from django.utils.translation import gettext_lazy as _

from Core.models.Element import Element

class ReportElementsDiagramPlotter():
    
    dicts = []

    @property
    def get_dict(self):
        return self.dicts

    @property
    def get_children(self):
        return self.element.get_children()

    @property
    def get_family(self):
        return self.element.get_family()

    @property
    def get_root(self):
        return self.element.get_root()

    @property
    def get_descendants(self, include_self=False):
        return self.element.get_descendants(include_self=include_self)
    
    @property
    def get_descendant_count(self):
        return self.element.get_descendant_count()

    @property
    def get_ancestors(self, ascending=False, include_self=False):
        return self.element.get_ancestors(ascending=ascending, include_self=include_self)

    def __init__(self, element_id: int, current_id=None, specific_node_tree=None):

        self.specific_node_tree = specific_node_tree if specific_node_tree else None
        self.current_element_id = current_id

        try:
            self.element = Element.objects.get(pk=element_id)
            self.dicts.clear()
            self.get_specific_tree()
            self.prepare()
        except:
            pass
    
    def get_specific_tree(self):
        if self.specific_node_tree:
            self.specific_nodes_ids = self.specific_node_tree.get_ancestors(ascending=True, include_self=True).values_list('pk', flat=True)

    def prepare(self):
        self.dicts = self.recursive_element_to_dict(self.element)
    
    def recursive_element_to_dict(self, element):

        result = {
            'id': element.pk,
            'name': _(element.code),
            'title': element.order,
            'children': []
        }

        if self.specific_node_tree and self.specific_nodes_ids :
            result['children'] = [self.recursive_element_to_dict(act) for act in element.get_children().order_by('-order') if act.pk in self.specific_nodes_ids]
        else:
            result['children'] = [self.recursive_element_to_dict(act) for act in element.get_children().order_by('-order')]

        return result
