from django.utils.translation import gettext_lazy as _
import datetime

from Core.models.Component import Component
from Core.models.Day import Day

from Core.control.DateTimeController import DateTimeController
from Core.control.DayControl import DayControl

from Core.procedures.PrepareProcedureObject import PrepareProcedureObject

class LogControl:

    def __init__(self, component_name: str, procedure_code: str, object, start_date: datetime, end_date=datetime, request=None):

        self.component = Component.objects.get(name=component_name)
        self.object = object
        self.procedure = PrepareProcedureObject(procedure_code=procedure_code,connected_object=self.object).instantiate_object()
        self.start_date = start_date
        self.end_date = end_date
        self.request = request

        DayControl().days_series(
            required_date=max(self.start_date, self.end_date),
            request=self.request)

    def create_log(self):
        self.procedure.log()
