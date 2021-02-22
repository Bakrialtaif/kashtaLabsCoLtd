from django.utils.translation import gettext_lazy as _
from Core.models.Component import Component

from Core.models.Element import Element
from Core.models.Fact import Fact
from Core.models.Analyze import Analyze
from Core.models.Procedure import Procedure

from Core.cons.PRESENTATION import list_of_component_types
from Core.cons.REPORT import list_of_element_types
from Core.cons.REPORT import list_of_report_types

class ComponentDiagramPlotter():
    
    component = None
    dicts = []

    @property
    def get_dict(self):
        return self.dicts

    @property
    def get_children(self):
        return self.component.get_children()

    @property
    def get_family(self):
        return self.component.get_family()

    @property
    def get_root(self):
        return self.component.get_root()

    @property
    def get_descendants(self, include_self=False):
        return self.component.get_descendants(include_self=include_self)
    
    @property
    def get_descendant_count(self):
        return self.component.get_descendant_count()

    @property
    def get_ancestors(self, ascending=False, include_self=False):
        return self.component.get_ancestors(ascending=ascending, include_self=include_self)

    def __init__(self, component_id: int, current_id=None, specific_node_tree=None, procedure_id=None):

        self.specific_node_tree = specific_node_tree if specific_node_tree else None
        self.current_component_id = current_id
        self.procedure_id = procedure_id if procedure_id else False

        try:
            self.component = Component.objects.get(pk=component_id)
            self.dicts.clear()
            self.get_specific_tree()
            self.prepare()
        except:
            pass
    
    def get_specific_tree(self):
        if self.specific_node_tree:
            self.specific_nodes_ids = self.specific_node_tree.get_ancestors(ascending=True, include_self=True).values_list('pk', flat=True)

    def prepare(self):
        self.dicts = self.recursive_component_to_dict(self.component)
    
    def recursive_component_to_dict(self, component):

        result = {
            'id': component.type,
            'name': '',
            'title': _(component.name),
            'children': []
        }

        if self.specific_node_tree and self.specific_nodes_ids :
            if component.get_children().count():
                result['children'] = [self.recursive_component_to_dict(act) for act in component.get_children().filter(show_in_menu=True).order_by('-order') if act.pk in self.specific_nodes_ids]
            else:
                if self.procedure_id:
                    procedure = Procedure.objects.get(pk=self.procedure_id)
                    result['children'] = [{'id': 'procedure', 'name': procedure.get_name, 'title': '', 'children': []}]
        else:
            if component.get_children().filter(show_in_menu=True).count():
                result['children'] = [self.recursive_component_to_dict(act) for act in component.get_children().filter(show_in_menu=True).order_by('-order')]
            else:
                result['children'] = self.loop_throw_procedures(component=component)

        return result

    def loop_throw_procedures(self, component):
    
        pro_list = []

        for procedure in component.procedures.all():
            pro_list.append({'id': 'procedure', 'name': procedure.get_name, 'title': '', 'children': []})

        return pro_list


class DimensionStatistics():

    def calculate(self):
        data = []
        for dimension in Element.objects.filter(type=list_of_element_types().DIMENSION).all():
            data.append({
                'dimension': dimension,
                'context_number': Element.objects.filter(type=list_of_element_types().CONTEXT, parent__pk=dimension.pk).count(),
                'cases_number': Element.objects.filter(type=list_of_element_types().CASE, parent__parent__pk=dimension.pk).count(),
                'facts_number': Fact.objects.filter(element__parent__parent__pk=dimension.pk).count(),
                'indicators_number': Analyze.objects.filter(type=list_of_report_types().INDICATOR ,element__parent__parent__pk=dimension.pk).count(),
                'sheet_numbers': Analyze.objects.filter(type=list_of_report_types().SHEET ,element__parent__parent__pk=dimension.pk).count(),
                'diagrams_number': Analyze.objects.filter(type=list_of_report_types().DIAGRAM ,element__parent__parent__pk=dimension.pk).count(),
            })
        return data

class ProgramProceduresDiagramPlotter():
    
    dicts = []

    @property
    def get_dict(self):
        return self.dicts

    @property
    def get_children(self):
        return self.component.get_children()

    @property
    def get_family(self):
        return self.component.get_family()

    @property
    def get_root(self):
        return self.component.get_root()

    @property
    def get_descendants(self, include_self=False):
        return self.component.get_descendants(include_self=include_self)
    
    @property
    def get_descendant_count(self):
        return self.component.get_descendant_count()

    @property
    def get_ancestors(self, ascending=False, include_self=False):
        return self.component.get_ancestors(ascending=ascending, include_self=include_self)

    def __init__(self, program_id: int):

        self.program_id = program_id

        try:
            self.program = Component.objects.get(pk=self.program_id, type=list_of_component_types().PROGRAM)
            self.dicts.clear()
            self.prepare()
        except:
            pass
    
    def prepare(self):
        self.dicts = self.recursive_component_to_dict(self.program)
    
    def recursive_component_to_dict(self, component):

        result = {
            'id': component.pk,
            'name': '',
            'title': _(component.name),
            'children': []
        }

        if component.get_children().count():
            result['children'] = [self.recursive_component_to_dict(act) for act in component.get_children()]
        else:
            result['children'] = self.loop_throw_procedures(component=component)

        return result

    def loop_throw_procedures(self, component):

        pro_list = []

        for procedure in component.procedures.all():
            pro_list.append({'id': 'procedure', 'name': procedure.code, 'title': '', 'children': []})

        return pro_list