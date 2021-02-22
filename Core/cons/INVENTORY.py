from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict


class list_of_item_types():
    
    CATEGORY = 'CATEGORY'
    ITEM = 'ITEM'

    @property
    def list(self):
        return {
            self.CATEGORY: _('CATEGORY'),
            self.ITEM: _('ITEM'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_inventory_operation_types():

    PURCHASE = 'PURCHASE'
    PAYMENT = 'PAYMENT'

    @property
    def list(self):
        return {
            self.PURCHASE: _('PURCHASE'),
            self.PAYMENT: _('PAYMENT'),
            }

    @property
    def iteratable(self):
        return self.list.items()

