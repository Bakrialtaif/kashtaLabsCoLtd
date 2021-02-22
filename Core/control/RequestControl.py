from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest
from datetime import datetime

from django.contrib.auth.models import User
from Core.models.Organization import Organization
from Core.models.Component import Component
from Core.models.WF_Chart import WF_Chart
from Core.models.WF_Action import WF_Action
from Core.models.WF_Input import WF_Input
from Core.models.WF_Data import WF_Data
from Core.models.WF_Request import WF_Request
from Core.models.WF_Track import WF_Track
from Core.models.WF_Dump import WF_Dump
from Core.models.Task import Task
from P001.models.Profile import Profile
from P003.models.Permission import Permission
from P013.models.OperationalPlan import OperationalPlan
from P013.models.Project import Project
from P013.models.Member import Member

from Core.cons.GENERAL import list_of_model_names
from Core.cons.WORKFLOW import list_of_action_types
from Core.cons.WORKFLOW import list_of_request_status
from Core.cons.WORKFLOW import list_of_priority_types
from Core.cons.WORKFLOW import list_of_executor_types
from Core.cons.WORKFLOW import list_of_input_choices
from Core.cons.WORKFLOW import list_of_action_categories
from Core.cons.TASK import list_of_task_types
from Core.cons.TASK import list_of_executions_status

from Core.control.DateTimeController import DateTimeController

class RequestControl:

    def __init__(self, request_params: HttpRequest, request_object: WF_Request):

        self.http_request = request_params
        self.request = request_object
        self.chart = self.request.chart
        self.current_action = self.request.action
        self.actions = WF_Action.objects.getActions(self.request.chart.pk)

        # None
        self.next_action = None

    def send(self):

        if self.current_action is None:
            
            self.chart = self.request.component.active_chart

            start_action = WF_Action.objects.getStartAction(self.chart.pk).get()
            first_action = WF_Action.objects.filter(chart=self.chart, parent=start_action).get()

            self.request.chart = self.chart
            self.request.sended_by = self.http_request.user
            self.request.sended_at = datetime.now()
            self.request.status = list_of_request_status.UNDER_PROCESS
            self.request.action = first_action
            self.request.task = self.create_workflow_task(first_action)
            self.request.save()

        return True

    def cancel(self):

        self.request.status = list_of_request_status().NOT_SEND
        self.request.action = None
        self.request.sended_by = None
        self.request.save()
        Task.objects.filter(request=self.request).delete()

        return True

    def move_forward(self):

        if self.request.status == list_of_request_status().UNDER_PROCESS:

            self.request.task.execution_status = list_of_executions_status().DONE
            self.request.task.save()

            # Do procedure finish stuff
            if self.request.action.category == list_of_action_categories().PROCEDURE:
                self.request.get_procedure.process_end()

            next_action = self.get_chart_next_action()

            if next_action.type == list_of_action_types().END:

                self.request.status = list_of_request_status().FINISHED
                self.request.action = next_action
                self.request.success = self.success_check()
                self.request.task = None
                self.request.save()

                self.request.finalize()

                # self.request_post_actions()

            else:

                self.request.status = list_of_request_status().UNDER_PROCESS
                self.request.action = next_action
                self.request.task = self.create_workflow_task(next_action)
                self.request.save()

    def move_backward(self):
        if self.request.status == list_of_request_status().UNDER_PROCESS and self.current_action.parent.type != list_of_action_types().START:
            self.request.action = self.current_action.parent
            self.request.task = Task.objects.filter(chart=self.request.chart,action=self.request.action,request=self.request).get()
            self.request.save()
            self.request.task.execution_status = list_of_executions_status().PROCESSING
            self.request.task.save()
            self.request.task.alert.not_visited()

        for action in self.request.action.get_descendants():
            Task.objects.filter(request=self.request, action=action).delete()

    # functions ****************************************************************

    def get_chart_next_action(self):
    
        if self.current_action.type == list_of_action_types().WITHOUT_CHILDREN:
            return WF_Action.objects.filter(parent=self.current_action,type=list_of_action_types().END).get()

        elif self.current_action.type == list_of_action_types().WITH_CHILD:
            return WF_Action.objects.getActions(self.chart.pk).filter(
                parent=self.current_action
                ).exclude(
                    type__in=[list_of_action_types().START, list_of_action_types().END]
                ).get()

        elif self.current_action.type == list_of_action_types().WITH_CHILDREN:            
            return self.current_action.branching_input.data.first().track.redirect_to


    def save_action_data(self):

        for item in self.http_request.POST:
            if item not in ['csrfmiddlewaretoken', 'execution_status'] and self.http_request.POST[item]:
                input = WF_Input.objects.get(pk=item.split('_')[1])

                if input.type == list_of_input_choices().MODELCHOICEFIELD:
                    WF_Data.objects.update_or_create(
                        action=self.request.action,
                        request=self.request,
                        task=self.request.task,
                        input=input,
                        defaults={
                            'value':None,
                            'track': WF_Track.objects.get(pk=self.http_request.POST[item])
                        }
                    )
                else:
                    WF_Data.objects.update_or_create(
                        action=self.request.action,
                        request=self.request,
                        task=self.request.task,
                        input=input,
                        defaults={
                            'value':self.http_request.POST[item],
                            'track': None
                        }
                    )

        if self.http_request.POST['execution_status']:
            self.request.task.execution_status = self.http_request.POST['execution_status']
            self.request.task.execution_date = datetime.now()
            self.request.task.save()
            
    def over_lab_validation(self):
        pass

    # helpers ******************************************************************

    def success_check(self):
        return True if WF_Data.objects.filter(
            action=self.request.action.parent,
            request=self.request,
            input=self.request.action.parent.success_input,
            value=self.request.action.parent.success_track
            ).count() else False

    def create_workflow_task(self, task_action: WF_Action):
        return Task.objects.create(
            type=list_of_task_types().WORKFLOW,
            chart=self.request.chart,
            action=task_action,
            request=self.request,
            name= '%s, %s, %s' % (_(self.request.component.content_type.model), self.request.action, self.request.user),
            assigned_by=self.http_request.user,
            assigned_to=self.get_task_executor(task_action),
            assigned_date=datetime.now(),
            duration=task_action.duration,
            end_date=DateTimeController().get_end_date(datetime.now(),self.request.action.duration),
            priority=list_of_priority_types().NOT_IMPORTANT_AND_NOT_URGENT,
            execution_status=list_of_executions_status().PROCESSING,
            execution_date=None
        )

    def get_task_executor(self, task_action: WF_Action):
        if task_action.executor_type == list_of_executor_types().SPECIFIC_EMPLOYEE:
            #DONE
            return task_action.executor
        elif task_action.executor_type == list_of_executor_types().REQUEST_CREATOR:
            #DONE
            return self.request.created_by.pk
        elif task_action.executor_type == list_of_executor_types().REQUEST_CREATOR_DIRECT_BOSS:
            #TODO
            return self.http_request.user
        elif task_action.executor_type == list_of_executor_types().REQUEST_CREATOR_UNIT_MANAGER:
            #TODO
            return self.http_request.user
        elif task_action.executor_type == list_of_executor_types().REQUEST_OWNER:
            #DONE
            return self.request.user.pk
        elif task_action.executor_type == list_of_executor_types().REQUEST_OWNER_DIRECT_BOSS:
            #TODO
            return self.http_request.user
        elif task_action.executor_type == list_of_executor_types().REQUEST_OWNER_UNIT_MANGER:
            #TODO
            return self.http_request.user
        elif task_action.executor_type == list_of_executor_types().FROM_RECORD:
            #TODO
            return self.http_request.user

    def request_post_actions(self):
        if self.request.component.content_type.model == list_of_model_names().PERMISSION:
            pass
        elif self.request.component.content_type.model == list_of_model_names().WF_DUMP:
            pass
        elif self.request.component.content_type.model == list_of_model_names().OPERATIONAL_PLAN:
            OperationalPlan.objects.filter(pk=self.request.operational_plan.pk).update(approved=True)
            for project in Project.objects.filter(operational_project__operational_plan__pk=self.request.operational_plan.pk).all():
                Member.objects.create(
                project=project,
                user=project.manager,
                responsibility='',
                privileges='',
                order=1)