from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_sex_types():
    
    MALE = 'MALE'
    FEMALE = 'FEMALE'

    @property
    def list(self):
        return {
            self.MALE: _('MALE'),
            self.FEMALE: _('FEMALE'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_martial_status():
    
    SINGLE = 'SINGLE'
    MARIED = 'MARIED'
    DIVORCEE = 'DIVORCEE'
    WIDOW = 'WIDOW'
    SUSPENDED = 'SUSPENDED'

    @property
    def list(self):
        return {
            self.SINGLE: _('SINGLE'),
            self.MARIED: _('MARIED'),
            self.DIVORCEE: _('DIVORCEE'),
            self.WIDOW: _('WIDOW'),
            self.SUSPENDED: _('SUSPENDED'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_health_status():

    NORMAL = 'NORMAL'
    IMPAIRED_HEARING = 'IMPAIRED_HEARING'
    IMPAIRED_MOBILITY = 'IMPAIRED_MOBILITY'
    VISUAL_IMPAIRMENT = 'VISUAL_IMPAIRMENT'
    INTELLECTUAL_DISABILITY = 'INTELLECTUAL_DISABILITY'
    MULTIPLE_DISABILITY = 'MULTIPLE_DISABILITY'
    MENTALILLNESS = 'MENTALILLNESS'
    TEMPORARY_DISCEASE = 'TEMPORARY_DISCEASE'
    CHRONIC_DISEASE = 'CHRONIC_DISEASE'


    @property
    def list(self):
        return {
            # self.NORMAL: _('NORMAL'),
            self.IMPAIRED_HEARING: _('IMPAIRED_HEARING'),
            self.IMPAIRED_MOBILITY: _('IMPAIRED_MOBILITY'),
            self.VISUAL_IMPAIRMENT: _('VISUAL_IMPAIRMENT'),
            self.INTELLECTUAL_DISABILITY: _('INTELLECTUAL_DISABILITY'),
            # self.MULTIPLE_DISABILITY: _('MULTIPLE_DISABILITY'),
            self.MENTALILLNESS: _('MENTALILLNESS'),
            self.TEMPORARY_DISCEASE: _('TEMPORARY_DISCEASE'),
            self.CHRONIC_DISEASE: _('CHRONIC_DISEASE'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_work_status():
    
    WORKING = 'WORKING'
    NOT_WORKING = 'NOT_WORKING'
    STUDENT = 'STUDENT'
    NOT_WILLING_TO_WORK = 'NOT_WILLING_TO_WORK'
    NOT_ABLE_TO_WORK = 'NOT_ABLE_TO_WORK'

    @property
    def list(self):
        return {
            self.WORKING: _('WORKING'),
            self.NOT_WORKING: _('NOT_WORKING'),
            self.STUDENT: _('STUDENT'),
            self.NOT_WILLING_TO_WORK: _('NOT_WILLING_TO_WORK'),
            self.NOT_ABLE_TO_WORK: _('NOT_ABLE_TO_WORK'),
            }

    @property
    def iteratable(self):
        return self.list.items()

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