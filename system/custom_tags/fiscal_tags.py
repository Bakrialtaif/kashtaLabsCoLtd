from django import template
from decimal import Decimal

from Core.models.Organization import Organization
from P011.control.FiscalControl import TreeOfAccountsDiagramPlotter
from P011.control.FiscalControl import TreeOfCostCentersDiagramPlotter
from P007.control.InventoryControl import TreeOfInventoryCategoriesAndItemsDiagramPlotter

from P011.cons.FISCAL import list_of_voucher_types
from P011.forms import VouchersSpecificationsForm

register = template.Library()

# Custom Tags ******************************************************************

@register.inclusion_tag('custom_tags/fiscal_tags/TreeOfAccountsDiagram.html')
def TreeOfAccountsDiagram(account_id, containerId, specific_node_tree=None):
    return {
        'diagram': TreeOfAccountsDiagramPlotter(account_id=account_id, specific_node_tree=specific_node_tree),
        'containerId': containerId
        }

@register.inclusion_tag('custom_tags/fiscal_tags/TreeOfCostCentersDiagram.html')
def TreeOfCostCentersDiagram(cost_center_id, containerId, specific_node_tree=None):
    return {
        'diagram': TreeOfCostCentersDiagramPlotter(cost_center_id=cost_center_id, specific_node_tree=specific_node_tree),
        'containerId': containerId
        }

@register.inclusion_tag('custom_tags/fiscal_tags/TreeOfInventoryCategoriesAndItemsDiagram.html')
def TreeOfInventoryCategoriesAndItemsDiagram(item_id, containerId, specific_node_tree=None):
    return {
        'diagram': TreeOfInventoryCategoriesAndItemsDiagramPlotter(item_id=item_id, specific_node_tree=specific_node_tree),
        'containerId': containerId
        }

@register.inclusion_tag('custom_tags/fiscal_tags/VouchersSpecifications.html', takes_context=True)
def VouchersSpecifications(context):
    return {
        'data': context['request'],
        'form': VouchersSpecificationsForm(initial={
            "voucher_type": context['request'].user.profile.get_vouchers_specifications,
            "voucher_status": context['request'].user.profile.get_vouchers_specifications,
            "fiscal_years": context['request'].user.profile.get_vouchers_specifications,
            })
        }

@register.inclusion_tag('custom_tags/fiscal_tags/EntriesMenu.html')
def EntriesMenu(status):
    return {
        'OPENING': list_of_voucher_types().OPENING,
        'GENERAL': list_of_voucher_types().GENERAL,
        'RECEIPT': list_of_voucher_types().RECEIPT,
        'PAYMENT': list_of_voucher_types().PAYMENT,
        'SETTLEMENT': list_of_voucher_types().SETTLEMENT,
        'CLOSING': list_of_voucher_types().CLOSING,
        'status': status,
    }        

# Custom Filter ****************************************************************
