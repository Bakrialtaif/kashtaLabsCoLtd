from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.urls import NoReverseMatch

from Core.procedures.ProcedureABC import ProcedureABC
from Core.models.Organization import Organization
from Core.models.Component import Component
from Core.models.Procedure import Procedure

from Core.models.Day import Day
from Core.models.Log import Log

class permission_request_procedure(ProcedureABC):

    def __init__(self, connected_object=None):

        self.code = self.__class__.__name__
        self.name = _(self.code)
        self.about = _('%s_about' % (self.code))
        self.procedure = Procedure.objects.get(code=self.code)
        self.component = self.procedure.component
        self.menu = self.component.parent
        self.program = self.menu.parent
        self.package = self.program.parent
        self._checks = []
        self.connected_object = connected_object
        self.path = '#'
        
    # Procedure Basic Logic ----------------------------------------------------

    def get_path(self, back_url):
        pass

    def process_start(self):
        pass

    def process_end(self):
        pass

    def status(self):
        return False if len(self.do_tests().checks_false) else True

    def log(self):
        Log.objects.create(
            component=self.component,
            user=self.connected_object.user,
            day=Day.objects.get(date=self.connected_object.date),
            permission=self.connected_object
        )

    def failures(self):
        return self.do_tests().checks_false

    @property
    def checks(self):
        return self._checks

    @property
    def checks_true(self):
        return [check for check in self._checks if check['status'] ]

    @property
    def checks_false(self):
        return [check for check in self._checks if not check['status'] ]

    def do_tests(self):
        [ eval("self.%s()" % (func)) for func in dir(self) if callable(getattr(self, func)) and func.startswith("test_")]
        return self

    # Procedure Custom Logic
    
    # Tests

    def test_nothing(self):
        pass