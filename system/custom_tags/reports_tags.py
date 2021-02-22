from django import template
from decimal import Decimal

from Core.control.ReportControl import ReportElementsDiagramPlotter

register = template.Library()

# Reports Tags ******************************************************************

@register.inclusion_tag('custom_tags/reports_tags/ReportElementsDiagram.html')
def ReportElementsDiagram(element_id, containerId, current_id=None, specific_node_tree=None):
    return {
        'diagram': ReportElementsDiagramPlotter(element_id=element_id, current_id=current_id, specific_node_tree=specific_node_tree),
        'containerId': containerId
        }
# Custom Filter ****************************************************************
