from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_component_types():
    
    START = 'START'
    PACKAGE = 'PACKAGE'
    PROGRAM = 'PROGRAM'
    MENU = 'MENU'
    OPERATION = 'OPERATION'    

    @property
    def list(self):
        return {
            self.START: _('START'),
            self.PACKAGE: _('PACKAGE'),
            self.PROGRAM: _('PROGRAM'),
            self.MENU: _('MENU'),
            self.OPERATION: _('OPERATION')
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_paragraph_types():
    
    INTRO = 'INTRO'
    ECOSYSTEM = 'ECOSYSTEM'
    METHODOLOGIES = 'METHODOLOGIES'
    TOOLS = 'TOOLS'
    PLAN = 'PLAN'
    MEMBER = 'MEMBER'
    FEATURES = 'FEATURES'

    @property
    def list(self):
        return {
            self.INTRO: _('INTRO'),
            self.ECOSYSTEM: _('ECOSYSTEM'),
            self.METHODOLOGIES: _('METHODOLOGIES'),
            self.TOOLS: _('TOOLS'),
            self.PLAN: _('PLAN'),
            self.MEMBER: _('MEMBER'),
            self.FEATURES: _('FEATURES'),
        }

    @property
    def iteratable(self):
        return self.list.items()        