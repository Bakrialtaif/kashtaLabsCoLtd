from django.utils.translation import gettext_lazy as _
from django.db.models import Count

from django.contrib.auth.models import User
from Core.models.Component import Component

from Core.models.WF_Request import WF_Request
from Core.models.WF_Chart import WF_Chart
from Core.models.WF_Action import WF_Action
from Core.models.WF_Input import WF_Input
from Core.models.WF_Track import WF_Track

from Core.cons.WORKFLOW import list_of_executor_types
from Core.cons.WORKFLOW import list_of_input_choices
from Core.cons.WORKFLOW import list_of_action_types
from Core.cons.WORKFLOW import list_of_action_categories

class WorkflowControl():

    def formObject(self, component_name: str, request_owner: User):

        self.component = Component.objects.filter(name=component_name).get()
        return {
            'component': self.component,
            'requests': WF_Request.objects.filter(component=self.component).all()
        }

    def createChartStartAction(self, chart: WF_Chart):

        action = WF_Action.objects.create(
            chart_id = chart.pk,
            name=_("start"),
            type= list_of_action_types().START,
            detail='',
            parent=None,
            executor_type='SPECIFIC_EMPLOYEE',
            executor=None,
            branching_input=None,
            notification_type='NOTIFICATION',
            order=0
        )

        self.createChartEndAction(WF_Action.objects.get(pk=action.pk))

        return False

    def createChartEndAction(self, action: WF_Action):
    
        WF_Action.objects.create(
            chart=WF_Chart.objects.get(pk=action.chart.pk),
            name=_("end"),
            type= list_of_action_types().END,
            detail='',
            parent= WF_Action.objects.get(pk=action.pk),
            executor_type='SPECIFIC_EMPLOYEE',
            executor=None,
            branching_input=None,
            notification_type='NOTIFICATION',
            order=99,
        )

        return False

    def reviewAllChartEndAction(self, chart_id: int):

        chart = WF_Chart.objects.get(pk=chart_id)

        # delete all END actions
        WF_Action.objects.filter(chart=chart, type=list_of_action_types().END).delete()

        # create END actions for actions without children
        for action in WF_Action.objects.filter(chart_id=chart_id).all():

            if action.type == list_of_action_types().START:

                if WF_Action.objects.filter(chart=chart).exclude(type__in=[list_of_action_types().START, list_of_action_types().END]).count() == 0:
                    self.createChartEndAction(action)

            else:

                child_number = WF_Action.objects.filter(chart=chart, parent=action).exclude(type__in=[list_of_action_types().START, list_of_action_types().END]).count()

                if child_number == 0:
                    self.createChartEndAction(action)
                    action.type = list_of_action_types().WITHOUT_CHILDREN;
                elif child_number == 1:
                    action.type = list_of_action_types().WITH_CHILD;
                elif child_number >= 2:
                    action.type = list_of_action_types().WITH_CHILDREN
                else:
                    pass


            action.save()

class chartCorrectionTests():

    def __init__(self, chart_id: int):
        
        self._chart_id = chart_id
        self._chart_object = WF_Chart.objects.get(pk=self._chart_id)
        self._chart_actions_list = WF_Action.objects.filter(chart=self._chart_object).exclude(type__in=[list_of_action_types().START, list_of_action_types().END]).order_by('pk')
        self._actions_with_branch = WF_Action.objects.filter(chart=self._chart_object, type=list_of_action_types().WITH_CHILDREN).exclude(type__in=[list_of_action_types().START, list_of_action_types().END])
        self._actions_with_success_condition = WF_Action.objects.filter(chart=self._chart_object, type=list_of_action_types().WITHOUT_CHILDREN).all()
        self._chart_actions_count = self._chart_actions_list.count()
        self._checks = []

        [ eval("self.%s()" % (func)) for func in dir(self) if callable(getattr(self, func)) and func.startswith("test_")]

        self.update_chart_status()

    def update_chart_status(self):

        if len(self.checks_false):

            self._chart_object.status = False
            self._chart_object.activation = False

        else:

            self._chart_object.status = True

        self._chart_object.save()

    @property
    def checks(self):
        return self._checks

    @property
    def checks_true(self):
        return [check for check in self._checks if check['status'] ]

    @property
    def checks_false(self):
        return [check for check in self._checks if not check['status'] ]

    def test_more_than_one_action(self):

        self._checks.append({
            'code': _("chart actions count"),
            'status': False if self._chart_actions_count == 0 else True,
            'message': _("chart actions number should be more than one")
        })

    def test_actions_executor(self):
        
        for action in self._chart_actions_list:

            if action.executor_type in list_of_executor_types().with_list:
    
                self._checks.append({
                    'code': action.name,
                    'status': True if action.executor else False,
                    'message': _("Action executor should be specified")
                })

    def test_actions_inputs_exist(self):
    
        for action in self._chart_actions_list:

            if action.category == list_of_action_categories().QUESTIONNAIRE:

                self._checks.append({
                    'code': action.name,
                    'status': False if action.inputs.count() == 0 else True,
                    'message': _("Action input should be one or more")
                })

    def test_success_condition_action(self):

        for action in self._actions_with_success_condition:

            if action.category == list_of_action_categories().QUESTIONNAIRE:

                self._checks.append({
                    'code': _("action success condition"),
                    'status': True if action.success_input and action.success_track else False,
                    'message': '%s: %s' % (action, _("action success condition must specified"))
                })

    def test_actions_with_branch(self):

        check = True
        for action in self._actions_with_branch:
    
            if action.branching_input == None:
                check = False
            else:
                for track in action.branching_input.tracks.all():
                    if not track.redirect_to:
                        check = False

            self._checks.append({
                'code': _("branch not prepared correctelly"),
                'status': True if check else False,
                'message': "%s : %s" % (action.name, _("branch not prepared correctelly"))
            })

class ChartDiagramPlotter():

    action = None
    dicts = []

    @property
    def get_dict(self):
        return self.dicts

    @property
    def get_children(self):
        return self.action.get_children()

    @property
    def get_family(self):
        return self.action.get_family()

    @property
    def get_root(self):
        return self.action.get_root()

    @property
    def get_descendants(self, include_self=False):
        return self.action.get_descendants(include_self=include_self)
    
    @property
    def get_descendant_count(self):
        return self.action.get_descendant_count()

    @property
    def get_ancestors(self, ascending=False, include_self=False):
        return self.action.get_ancestors(ascending=ascending, include_self=include_self)

    def __init__(self, action_id: int, current_id: int):
        self.action = WF_Action.objects.get(pk=action_id)
        self.current_action_id = current_id
        self.dicts.clear()
        self.prepare()

    def prepare(self):
        self.dicts = self.recursive_action_to_dict(self.action)
    
    def recursive_action_to_dict(self, action):

        if action.type in [list_of_action_types().START, list_of_action_types().END]:
            id = action.type.lower()
        elif action.pk == self.current_action_id:
            id = 'current'
        else:
            id = action.pk
    
        result = {
            'id': id,
            'name': action.get_name,
            'title': _(action.executor_type) if action.type not in [list_of_action_types().START, list_of_action_types().END] else _('the action'),
            'children': []
        }

        result['children'] = [self.recursive_action_to_dict(act) for act in action.get_children().order_by('-order')]
        return result

class actionLogicOperator():

    _action = None
    _inputs = None
    _operator_list = []

    # operators
    _equal = '='
    _gte = '>='
    _ste = '<='

    def __init__(self, action: WF_Action):

        # initialize data variable
        self._action = action
        self._inputs = action.inputs.all()

        # execute class methods
        self._input_operator_list()
        self._update_action_with_logic_operator()

    def _input_operator_list(self):

        x=1
        for _input in self._inputs:

            if _input.type in list_of_input_choices().MODELCHOICEFIELD:
                pass

                # for item in list_of_dropdowns().getList(_input.list):
                #     self._operator_list.append({'counter': x,'code': self._equal,'value': item[0]})
                # pass

            if _input.type in list_of_input_choices().INTEGERFIELD:
                pass

            if _input.type in list_of_input_choices().FLOATFIELD:
                pass

            if _input.type in list_of_input_choices().BOOLEANFIELD:
                pass

    def _update_action_with_logic_operator(self):
        self._action.logic_operators = self._input_operator_list
        self._action.save()

class UpdateActionBranchingTracks():

    action = None
    input = None

    def __init__(self, action: WF_Action, input: WF_Input):
        self.action = action
        self.input = input

        self.updateActionBranchingInput()
        self.removeOldTracks()
        # self.createInputTracks()

    def updateActionBranchingInput(self):
        WF_Action.objects.filter(pk=self.action.pk).update(branching_input=WF_Input.objects.get(pk=self.input.pk))

    def removeOldTracks(self):
        WF_Track.objects.filter(action=self.action).delete()