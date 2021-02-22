from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict


class list_of_box_types():
    
    INBOX = 'INBOX'
    OUTBOX = 'OUTBOX'

    @property
    def list(self):
        return {
            self.INBOX: _('INBOX'),
            self.OUTBOX: _('OUTBOX'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_folder_types():
    
    ORGANIZATION_INBOX = 'ORGANIZATION_INBOX'
    ORGANIZATION_OUTBOX = 'ORGANIZATION_OUTBOX'
    ORGANIZATION_FOLDER = 'ORGANIZATION_FOLDER'
    EMPLOYEE_INBOX = 'EMPLOYEE_INBOX'
    EMPLOYEE_OUTBOX = 'EMPLOYEE_OUTBOX'
    EMPLOYEE_FOLDER = 'EMPLOYEE_FOLDER'

    @property
    def list(self):
        return {
            self.ORGANIZATION_INBOX: _('ORGANIZATION_INBOX'),
            self.ORGANIZATION_OUTBOX: _('ORGANIZATION_OUTBOX'),
            self.ORGANIZATION_FOLDER: _('ORGANIZATION_FOLDER'),
            self.EMPLOYEE_INBOX: _('EMPLOYEE_INBOX'),
            self.EMPLOYEE_OUTBOX: _('EMPLOYEE_OUTBOX'),
            self.EMPLOYEE_FOLDER: _('EMPLOYEE_FOLDER'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_referral_types():
    
    REFERRAL = 'REFERRAL'
    TASK = 'TASK'

    @property
    def list(self):
        return {
            self.REFERRAL: _('REFERRAL'),
            self.TASK: _('TASK'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_referral_privileges_types():
    
    EDIT = 'EDIT'
    REFERRAL = 'REFERRAL'
    ATTACHMENT = 'ATTACHMENT'

    @property
    def list(self):
        return {
            self.EDIT: _('EDIT'),
            self.REFERRAL: _('REFERRAL'),
            self.ATTACHMENT: _('ATTACHMENT'),
            }

    @property
    def iteratable(self):
        return self.list.items()        


# Translation

_("ORGANIZATION INBOX DESCRIPTION")
_("ORGANIZATION OUTBOX DESCRIPTION")
_("EMPLOYEE INBOX DESCRIPTION")
_("EMPLOYEE OUTBOX DESCRIPTION")