from django.utils.translation import gettext_lazy as _

import datetime

from Core.models.Component import Component
from Core.models.Day import Day
from Core.models.DayInWeek import DayInWeek

from Core.control.DateTimeController import DateTimeController

class DayControl:

    def days_series(self, required_date: datetime, request=None):

        if not Day.objects.filter(date=required_date).exists():

            for date_in_range in DateTimeController().get_daterange(start_date=request.organization.last_log_date, end_date=required_date, step=1):

                request.organization.days.update_or_create(
                    date=date_in_range,
                    day_in_week=DayInWeek.objects.get(value=date_in_range.weekday())
                )