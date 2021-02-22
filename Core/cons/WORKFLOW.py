from django.utils.translation import gettext_lazy as _
from django.utils.datastructures import MultiValueDict

class list_of_executor_types():

    FROM_RECORD = 'FROM_RECORD'
    REQUEST_OWNER = 'REQUEST_OWNER'
    REQUEST_OWNER_DIRECT_BOSS = 'REQUEST_OWNER_DIRECT_BOSS'
    REQUEST_OWNER_UNIT_MANGER = 'REQUEST_OWNER_UNIT_MANGER'
    REQUEST_CREATOR = 'REQUEST_CREATOR'
    REQUEST_CREATOR_DIRECT_BOSS = 'REQUEST_CREATOR_DIRECT_BOSS'
    REQUEST_CREATOR_UNIT_MANAGER = 'REQUEST_CREATOR_UNIT_MANAGER'
    ANY_UNIT_MANAGER = 'ANY_UNIT_MANAGER'
    SPECIFIC_EMPLOYEE = 'SPECIFIC_EMPLOYEE'

    @property
    def list(self):
        return {
            self.FROM_RECORD: _('FROM_RECORD'),
            self.REQUEST_OWNER: _('REQUEST_OWNER'),
            self.REQUEST_OWNER_DIRECT_BOSS: _('REQUEST_OWNER_DIRECT_BOSS'),
            self.REQUEST_OWNER_UNIT_MANGER: _('REQUEST_OWNER_UNIT_MANGER'),
            self.REQUEST_CREATOR: _('REQUEST_CREATOR'),
            self.REQUEST_CREATOR_DIRECT_BOSS: _('REQUEST_CREATOR_DIRECT_BOSS'),
            self.REQUEST_CREATOR_UNIT_MANAGER: _('REQUEST_CREATOR_UNIT_MANAGER'),
            self.ANY_UNIT_MANAGER: _('ANY_UNIT_MANAGER'),
            self.SPECIFIC_EMPLOYEE: _('SPECIFIC_EMPLOYEE')
            }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def with_message(self): 
        return {
            self.REQUEST_OWNER,
            self.REQUEST_OWNER_DIRECT_BOSS,
            self.REQUEST_OWNER_UNIT_MANGER,
            self.REQUEST_CREATOR,
            self.REQUEST_CREATOR_DIRECT_BOSS,
            self.REQUEST_CREATOR_UNIT_MANAGER
        }
    
    @property
    def with_list(self):
        return {
            self.SPECIFIC_EMPLOYEE,
            self.ANY_UNIT_MANAGER,
            self.FROM_RECORD
        }

class list_of_notification_types:

    NOTIFICATION = 'NOTIFICATION'
    EMAIL = 'EMAIL'
    SMS = 'SMS'

    @property
    def list(self):
        return {
            self.NOTIFICATION: _('NOTIFICATION'),
            self.EMAIL: _('EMAIL'),
            self.SMS: _('SMS'),
            }
            
    @property
    def iteratable(self):
        return self.list.items()

class list_of_action_categories:
    
    QUESTIONNAIRE = 'QUESTIONNAIRE'
    PROCEDURE = 'PROCEDURE'

    @property
    def list(self):
        return {
            self.QUESTIONNAIRE: _('QUESTIONNAIRE'),
            self.PROCEDURE: _('PROCEDURE'),
            }
            
    @property
    def iteratable(self):
        return self.list.items()        

class list_of_action_types:
    
    START = 'START'
    END = 'END'
    WITH_CHILD = 'WITH_CHILD'
    WITH_CHILDREN = 'WITH_CHILDREN'
    WITHOUT_CHILDREN = 'WITHOUT_CHILDREN'

    @property
    def list(self):
        return {
            self.START: _('START'),
            self.END: _('END'),
            self.WITH_CHILD: _('WITH_CHILD'),
            self.WITH_CHILDREN: _('WITH_CHILDREN'),
            self.WITHOUT_CHILDREN: _('WITHOUT_CHILDREN'),
            }
            
    @property
    def iteratable(self):
        return self.list.items()        

class list_of_input_choices:

    BOOLEANFIELD = 'BooleanField'
    CHARFIELD = 'CharField'
    TEXTAREAFIELD = 'TextAreaField'
    INTEGERFIELD = 'IntegerField'
    FLOATFIELD = 'FloatField'
    MODELCHOICEFIELD = 'ModelChoiceField'

    @property
    def list(self):
        return {
            self.BOOLEANFIELD: _('BOOLEANFIELD'),
            self.CHARFIELD: _('CHARFIELD'),
            self.TEXTAREAFIELD: _('TEXTAREAFIELD'),
            self.INTEGERFIELD: _('INTEGERFIELD'),
            self.FLOATFIELD: _('FLOATFIELD'),
            self.MODELCHOICEFIELD: _('MODELCHOICEFIELD'),
        }

    @property
    def iteratable(self):
        return self.list.items()

    @property
    def support_branching(self):
        return {
            self.BOOLEANFIELD,
            self.INTEGERFIELD,
            self.FLOATFIELD,
            self.MODELCHOICEFIELD
        }

class list_of_request_status:
    
    NOT_SEND = 'NOT_SEND'
    UNDER_PROCESS = 'UNDER_PROCESS'
    FINISHED = 'FINISHED'

    @property
    def list(self):
        return {
            self.NOT_SEND: _('NOT_SEND'),
            self.UNDER_PROCESS: _('UNDER_PROCESS'),
            self.FINISHED: _('FINISHED')
        }

    @property
    def iteratable(self):
        return self.list.items()

class list_of_request_move_types:
    
    FORWARD = 'FORWARD'
    BACKWARD = 'BACKWARD'

    @property
    def list(self):
        return {
            self.FORWARD: _('FORWARD'),
            self.BACKWARD: _('BACKWARD'),
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