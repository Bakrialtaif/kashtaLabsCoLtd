from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict


class list_of_task_types():
    
    WORKFLOW = 'WORKFLOW'
    PROJECT = 'PROJECT'
    COMMUNICATION = 'COMMUNICATION'

    @property
    def list(self):
        return {
            self.WORKFLOW: _('WORKFLOW'),
            self.PROJECT: _('PROJECT'),
            self.COMMUNICATION: _('COMMUNICATION'),
            }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_priority_types:
    
    IMPORTANT_AND_URGENT = 'IMPORTANT_AND_URGENT'
    IMPORTANT_AND_NOT_URGENT = 'IMPORTANT_AND_NOT_URGENT'
    NOT_IMPORTANT_AND_URGENT = 'NOT_IMPORTANT_AND_URGENT'
    NOT_IMPORTANT_AND_NOT_URGENT = 'NOT_IMPORTANT_AND_NOT_URGENT'

    @property
    def list(self):
        return {
            self.IMPORTANT_AND_URGENT: _('IMPORTANT_AND_URGENT'),
            self.IMPORTANT_AND_NOT_URGENT: _('IMPORTANT_AND_NOT_URGENT'),
            self.NOT_IMPORTANT_AND_URGENT: _('NOT_IMPORTANT_AND_URGENT'),
            self.NOT_IMPORTANT_AND_NOT_URGENT: _('NOT_IMPORTANT_AND_NOT_URGENT'),
        }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def colors(self):
        return {
            self.IMPORTANT_AND_URGENT: '#FE634E',
            self.IMPORTANT_AND_NOT_URGENT: '#F39629',
            self.NOT_IMPORTANT_AND_URGENT: '#2398AB',
            self.NOT_IMPORTANT_AND_NOT_URGENT: '#939598',
        }
    
    def get_color(self, priority):
        return self.colors[priority]
    
class list_of_executions_status:
    
    QUEUEING = 'QUEUEING'
    PROCESSING = 'PROCESSING'
    DONE = 'DONE'

    @property
    def list(self):
        return {
            self.QUEUEING: _('QUEUEING'),
            self.PROCESSING: _('PROCESSING'),
            self.DONE: _('DONE'),
        }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def colors(self):
        return {
            self.QUEUEING: '#939598',
            self.PROCESSING: '#F39629',
            self.DONE: '#88F0A0',
        }

    def get_color(self, priority):
        return self.colors[priority]

class list_of_completion_status:

    OPEN = 'OPEN'
    CLOSE = 'CLOSE'

    @property
    def list(self):
        return {
            self.OPEN: _('OPEN'),
            self.CLOSE: _('CLOSE'),
        }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def colors(self):
        return {
            self.OPEN: '#939598',
            self.CLOSE: '#88F0A0',
        }

    def get_color(self, priority):
        return self.colors[priority]