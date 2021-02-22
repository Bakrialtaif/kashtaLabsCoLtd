from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_element_types():

    START='START'
    DIMENSION='DIMENSION'
    CONTEXT='CONTEXT'
    CASE='CASE'
    
    @property
    def list(self):
        return {
            self.START: _('START'),
            self.DIMENSION: _('DIMENSION'),
            self.CONTEXT: _('CONTEXT'),
            self.CASE: _('CASE'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_report_types():
    
    INDICATOR='INDICATOR'
    SHEET='SHEET'
    DIAGRAM='DIAGRAM'
    
    @property
    def list(self):
        return {
            self.INDICATOR: _('INDICATOR'),
            self.SHEET: _('SHEET'),
            self.DIAGRAM: _('DIAGRAM'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_periodicity_types():
    
    DAILY='DAILY'
    WEEKLY='WEEKLY'
    MONTHLY='MONTHLY'
    YEARLY='YEARLY'
    
    @property
    def list(self):
        return {
            self.DAILY: _('DAILY'),
            self.WEEKLY: _('WEEKLY'),
            self.MONTHLY: _('MONTHLY'),
            self.YEARLY: _('YEARLY'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_dimension_types():
    
    ORGANIZATIONAL = 'ORGANIZATIONAL'
    OPERATIONAL = 'OPERATIONAL'
    FINANCIAL = 'FINANCIAL'
    CUSTOMERS = 'CUSTOMERS'
    LEARNING = 'LEARNING'
    GROWTH = 'GROWTH'

    @property
    def list(self):
        return {
            self.ORGANIZATIONAL: _('ORGANIZATIONAL'),
            self.OPERATIONAL: _('OPERATIONAL'),
            self.FINANCIAL: _('FINANCIAL'),
            self.CUSTOMERS: _('CUSTOMERS'),
            self.LEARNING: _('LEARNING'),
            self.GROWTH: _('GROWTH'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_datum_types():
    
    NUMERIC = 'NUMERIC'
    STRING = 'STRING'

    @property
    def list(self):
        return {
            self.NUMERIC: _('NUMERIC'),
            self.STRING: _('STRING'),
            }

    @property
    def iteratable(self):
        return self.list.items()