from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict


class list_of_education_levels():

    PRIMARY = 'PRIMARY' 
    INTERMEDIATE = 'INTERMEDIATE' 
    SECONDARY = 'SECONDARY' 
    BACHELOR = 'BACHELOR' 
    DIPLOMA = 'DIPLOMA' 
    HIGHER_DIPLOMA = 'HIGHER_DIPLOMA'
    MASTER = 'MASTER' 
    DOCTORATE = 'DOCTORATE' 

    @property
    def list(self):
        return {
            self.PRIMARY: _('PRIMARY'),
            self.INTERMEDIATE: _('INTERMEDIATE'),
            self.SECONDARY: _('SECONDARY'),
            self.BACHELOR: _('BACHELOR'),
            self.DIPLOMA: _('DIPLOMA'),
            self.HIGHER_DIPLOMA: _('HIGHER_DIPLOMA'),
            self.MASTER: _('MASTER'),
            self.DOCTORATE: _('DOCTORATE'),
            }

    @property
    def iteratable(self):
        return self.list.items()