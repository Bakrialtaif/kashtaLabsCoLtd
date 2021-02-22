from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_organization_types():
    
    OWNER = 'OWNER'
    CUSTOMER = 'CUSTOMER'
    SUPPLIER = 'SUPPLIER'

    @property
    def list(self):
        return {
            self.OWNER: _('OWNER'),
            self.CUSTOMER: _('CUSTOMER'),
            self.SUPPLIER: _('SUPPLIER'),
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_organization_user_types():
    
    CREATOR = 'CREATOR'
    USER = 'USER'

    @property
    def list(self):
        return {
            self.CREATOR: _('CREATOR'),
            self.USER: _('USER'),
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_unit_types():
    
    UNIT = 'UNIT'
    COMMITTEE = 'COMMITTEE'

    @property
    def list(self):
        return {
            self.UNIT: _('UNIT'),
            self.COMMITTEE: _('COMMITTEE'),
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_vacancy_types():
    
    EXECUTIVE = 'EXECUTIVE'
    SUPERVISORY = 'SUPERVISORY'
    SUPPORTSHIP = 'SUPPORTSHIP'
    INTERNSHIP = 'INTERNSHIP'
    VOLUNTEERSHIP = 'VOLUNTEERSHIP'
    

    @property
    def list(self):
        return {
            self.EXECUTIVE: _('EXECUTIVE'),
            self.SUPERVISORY: _('SUPERVISORY'),
            self.SUPPORTSHIP: _('SUPPORTSHIP'),
            self.INTERNSHIP: _('INTERNSHIP'),
            self.VOLUNTEERSHIP: _('VOLUNTEERSHIP'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_duty_types():
    
    DUTY ='DUTY'
    RESPONSIBILITY = 'RESPONSIBILITY'

    @property
    def list(self):
        return {
            self.DUTY: _('DUTY'),
            self.RESPONSIBILITY: _('RESPONSIBILITY'),
            }

    @property
    def iteratable(self):
        return self.list.items()
        

class list_of_vacancy_nature():
    
    BASIC ='BASIC'
    SECONDARY = 'SECONDARY'

    @property
    def list(self):
        return {
            self.BASIC: _('BASIC'),
            self.SECONDARY: _('SECONDARY'),
            }

    @property
    def iteratable(self):
        return self.list.items()