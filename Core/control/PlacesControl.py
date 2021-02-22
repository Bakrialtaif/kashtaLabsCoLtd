from django.utils.translation import gettext_lazy as _

from Core.models.Place import Place

class PlacesDiagramPlotter():
    
    top_place = None
    dicts = []

    @property
    def get_dict(self):
        return self.dicts

    @property
    def get_children(self):
        return self.top_place.get_children()

    @property
    def get_family(self):
        return self.top_place.get_family()

    @property
    def get_root(self):
        return self.top_place.get_root()

    @property
    def get_descendants(self, include_self=False):
        return self.top_place.get_descendants(include_self=include_self)
    
    @property
    def get_descendant_count(self):
        return self.top_place.get_descendant_count()

    @property
    def get_ancestors(self, ascending=False, include_self=False):
        return self.top_place.get_ancestors(ascending=ascending, include_self=include_self)

    def __init__(self, top_place_id: int, current_id=None, specific_node_tree=None):

        self.specific_node_tree = specific_node_tree if specific_node_tree else None

        try:
            self.top_place = Place.objects.get(pk=top_place_id)
            self.dicts.clear()
            self.get_specific_tree()
            self.prepare()
        except:
            pass
    
    def get_specific_tree(self):
        if self.specific_node_tree:
            self.specific_nodes_ids = self.specific_node_tree.get_ancestors(ascending=True, include_self=True).values_list('pk', flat=True)

    def prepare(self):
        self.dicts = self.recursive_top_place_to_dict(self.top_place)
    
    def recursive_top_place_to_dict(self, top_place):

        result = {
            'id': top_place.type,
            'name': top_place.name,
            'title': '',
            'children': []
        }

        if self.specific_node_tree and self.specific_nodes_ids :
            result['children'] = [self.recursive_top_place_to_dict(act) for act in top_place.get_children().order_by('-pk') if act.pk in self.specific_nodes_ids]
        else:
            result['children'] = [self.recursive_top_place_to_dict(act) for act in top_place.get_children().order_by('-pk')]

        return result