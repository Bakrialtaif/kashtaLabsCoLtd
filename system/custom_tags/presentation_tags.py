from django import template
register = template.Library()

from Core.models.Component import Component
from Core.cons.PRESENTATION import list_of_component_types
from Core.control.ComponentController import ComponentDiagramPlotter
from Core.control.ComponentController import ProgramProceduresDiagramPlotter

# Custom Tags ******************************************************************

@register.inclusion_tag('custom_tags/presentation_tags/package_menu.html')
def package_menu():
    return {
        'packages': Component.objects.filter(type=list_of_component_types().PACKAGE).order_by('order').all()
    }

@register.inclusion_tag('custom_tags/presentation_tags/ComponentDiagram.html')
def ComponentDiagram(component_id, containerId, current_id=None, procedure_id=None, specific_node_tree=None):
    return {
        'diagram': ComponentDiagramPlotter(component_id=component_id, current_id=current_id, specific_node_tree=specific_node_tree, procedure_id=procedure_id),
        'containerId': containerId
        }

@register.inclusion_tag('custom_tags/presentation_tags/ProceduresDiagram.html')
def ProceduresDiagram(program_id, containerId):
    return {
        'diagram': ProgramProceduresDiagramPlotter(program_id=program_id),
        'containerId': containerId
        }

# Custom Filter ****************************************************************
