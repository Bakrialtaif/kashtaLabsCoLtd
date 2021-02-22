from django import template
from django.db.models import Q, Count
from django.utils.crypto import get_random_string
from Core.models.Organization import Organization

from Core.models.WF_Chart import WF_Chart
from Core.models.WF_Action import WF_Action
from Core.forms import WF_XForm, WF_TaskForm

from Core.control.WorkflowControl import ChartDiagramPlotter
from Core.cons.WORKFLOW import list_of_request_status
from Core.cons.WORKFLOW import list_of_request_move_types
from Core.cons.WORKFLOW import list_of_action_types
from Core.cons.WORKFLOW import list_of_executions_status
from Core.cons.WORKFLOW import list_of_action_categories

register = template.Library()

@register.inclusion_tag('custom_tags/workflow_tags/request.html')
def request(request):
    return {'request': request}    

@register.inclusion_tag('custom_tags/workflow_tags/SendRequestLink.html')
def SendRequestLink(requestObject):
    return {
        'requestObject': requestObject,
        'not_send': list_of_request_status().NOT_SEND,
        }

@register.inclusion_tag('custom_tags/workflow_tags/CancelRequestLink.html')
def CancelRequestLink(requestObject):
    return {
        'requestObject': requestObject,
        'under_proccess': list_of_request_status().UNDER_PROCESS
        }

@register.inclusion_tag('custom_tags/workflow_tags/RequestTopLinks.html')
def RequestTopLinks(component, url, modal=False):
    return {
        'component': component,
        'url': url,
        'modal': modal
        }

@register.inclusion_tag('custom_tags/workflow_tags/RequestNote.html')
def RequestNote():
    return {}

@register.inclusion_tag('custom_tags/workflow_tags/RequestRowLinks.html')
def RequestRowLinks(request, status=False, browse=False, log=False):
    return {'request': request, 'status': status, 'browse': browse, 'log': log}
        
@register.inclusion_tag('custom_tags/workflow_tags/RequestBrowseWidget.html')
def RequestBrowseWidget(requestObject):
    return {
        'requestObject': requestObject,
        }

@register.inclusion_tag('custom_tags/workflow_tags/RequestProcessWidget.html')
def RequestProcessWidget(requestObject, procedure_code):
    return {
        'requestObject': requestObject,
        'procedure_code': procedure_code
        }

@register.inclusion_tag('custom_tags/workflow_tags/ActionForm.html', takes_context=True)
def ActionForm(context, requestObject, action_id):

    if action_id:
        form = WF_XForm(context['request'], action_id)
    else:
        form = None

    return {
        'form': form,
        'requestObject': requestObject,
        'with_children': list_of_action_types().WITH_CHILDREN
    }

@register.inclusion_tag('custom_tags/workflow_tags/ActionTaskForm.html', takes_context=True)
def ActionTaskForm(context, requestObject, action_id):

    if action_id:
        form = WF_TaskForm(context['request'], requestObject=requestObject, action_id=action_id)
    else:
        form = None

    return {
        'form': form,
        'requestObject': requestObject,
        'with_children': list_of_action_types().WITH_CHILDREN,
        'without_children': list_of_action_types().WITHOUT_CHILDREN,
        'end': list_of_action_types().END,
        'QUESTIONNAIRE': list_of_action_categories().QUESTIONNAIRE,
        'PROCEDURE': list_of_action_categories().PROCEDURE
    }

@register.inclusion_tag('custom_tags/workflow_tags/RequestData.html')
def RequestData(requestObject):
    return {'requestObject': requestObject}

@register.inclusion_tag('custom_tags/workflow_tags/RequestDocuments.html')
def RequestDocuments(requestObject):
    return {'requestObject': requestObject}

@register.inclusion_tag('custom_tags/workflow_tags/WorkflowChartDiagram.html')
def WorkflowChartDiagram(action_id, current_id, containerId):
    return {
        'diagram': ChartDiagramPlotter(action_id=action_id, current_id=current_id),
        'containerId': containerId
        }

@register.inclusion_tag('custom_tags/workflow_tags/RequestMoveForward.html')
def RequestMoveForward(requestObject):
    return {
        'requestObject': requestObject,
        'move_type': list_of_request_move_types().FORWARD.lower(),
        'under_proccess': list_of_request_status().UNDER_PROCESS,
        'done': list_of_executions_status().DONE,
        'QUESTIONNAIRE': list_of_action_categories().QUESTIONNAIRE,
        'PROCEDURE': list_of_action_categories().PROCEDURE
        }

@register.inclusion_tag('custom_tags/workflow_tags/RequestMoveBackward.html')
def RequestMoveBackward(requestObject):
    return {
        'requestObject': requestObject,
        'move_type': list_of_request_move_types().BACKWARD.lower(),
        'under_proccess': list_of_request_status().UNDER_PROCESS,
        'start': list_of_action_types().START,
        'QUESTIONNAIRE': list_of_action_categories().QUESTIONNAIRE,
        'PROCEDURE': list_of_action_categories().PROCEDURE
        }
        
@register.inclusion_tag('custom_tags/workflow_tags/RequestLog.html')
def RequestLog(requestObject, back_url):
    return {
        'requestObject': requestObject,
        'back_url': back_url,
        'not_send': list_of_request_status().NOT_SEND,
        }

@register.inclusion_tag('custom_tags/workflow_tags/ChartQuestionnaire.html', takes_context=True)
def ChartQuestionnaire(context, chartObject: WF_Chart):

    form_list = {}
    actions = WF_Action.objects.getActions(chart_id=chartObject.pk).annotate(input_num=Count('inputs')).order_by('order')
    for action in actions:
        form_list[action] = WF_XForm(context['request'], action.id)

    return {
        'actions': actions,
        'randId': get_random_string(length=15),
        'form_list': form_list,
        }        


        