from django import template
from decimal import Decimal

from P003.models.Folder import Folder
from Core.cons.ARCHIVE import list_of_folder_types

from P003.control.ArchiveController import ReferralDiagramPlotter

register = template.Library()

# Custom Tags ******************************************************************

@register.inclusion_tag('custom_tags/archive_tags/employee_folders_menu.html', takes_context=True)
def employee_folders_menu(context, current_folder_id=None):
    return {
        'basic_inboxes': Folder.objects.filter(user=context['request'].user, type__in=[list_of_folder_types().EMPLOYEE_INBOX, list_of_folder_types().EMPLOYEE_OUTBOX]).order_by('order').all(),
        'folders': Folder.objects.filter(user=context['request'].user, type=list_of_folder_types.EMPLOYEE_FOLDER).order_by('order').all(),
        'current_folder_id': current_folder_id
        }

@register.inclusion_tag('custom_tags/archive_tags/organization_folders_menu.html', takes_context=True)
def organization_folders_menu(context, current_folder_id=None):
    return {
        'basic_inboxes': Folder.objects.filter(user=None, type__in=[list_of_folder_types().ORGANIZATION_INBOX, list_of_folder_types().ORGANIZATION_OUTBOX]).order_by('order').all(),
        'folders': Folder.objects.filter(user=None, type=list_of_folder_types.ORGANIZATION_FOLDER).order_by('order').all(),
        'current_folder_id': current_folder_id
        }

@register.inclusion_tag('custom_tags/archive_tags/TransactionDocuments.html')
def TransactionDocuments(transactionObject):
    return {'transactionObject': transactionObject}        

@register.inclusion_tag('custom_tags/archive_tags/ReferralChartDiagram.html')
def ReferralChartDiagram(referral_id, containerId, current_id=None, specific_node_tree=None):
    return {
        'diagram': ReferralDiagramPlotter(referral_id=referral_id, current_id=current_id, specific_node_tree=specific_node_tree),
        'containerId': containerId
        }
# Custom Filter ****************************************************************
