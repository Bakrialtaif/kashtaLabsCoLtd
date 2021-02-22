from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_user_classification_types():

    EMPLOYEE = 'EMPLOYEE'
    CLIENT = 'CLIENT'

    @property
    def list(self):
        return {
            self.EMPLOYEE: _('EMPLOYEE'),
            self.CLIENT: _('CLIENT'),
        }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def beneficiary_classifications(self):
        return {
            self.CLIENT: _('CLIENT'),
        }
    
    @property
    def beneficiary_classifications_iteratable(self):
        return self.beneficiary_classifications.items()

    @property
    def general_classifications(self):
        return {
            self.EMPLOYEE: _('EMPLOYEE'),
        }
    
    @property
    def general_classifications_iteratable(self):
        return self.general_classifications.items()