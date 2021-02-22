from django.db.models import ForeignKey
from django.utils.translation import gettext_lazy as _

import datetime

class DateTimeController:
    
    def get_end_date(self, start_date: datetime, duration: int):
        return start_date + datetime.timedelta(days=duration)

    def get_daterange(self, start_date, end_date, step):
        delta = end_date - start_date
        return [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]

    def date_in_between(self, date: datetime, start_date: datetime, end_date: datetime):
        return True if start_date <= datetime.strptime(date, '%Y-%m-%d').date() <= end_date else False

    def time_diff_in_minutes(self, time_end: datetime, time_start: datetime):
        return (datetime.datetime.combine(datetime.date(1, 1, 1), time_end) - datetime.datetime.combine(datetime.date(1, 1, 1), time_start)).total_seconds() / 60
        
    def time_diff(self, time_end: datetime, time_start: datetime):
        return str(datetime.datetime.combine(datetime.date(1, 1, 1), time_end) - datetime.datetime.combine(datetime.date(1, 1, 1), time_start))

    def format_time(self, time_string: str):
        x = time_string.split(':')
        return '%s%s,%s%s' % (x[0], _('H'), x[1], _('M'))

    def format_minutes_to_hour_minutes(self, minutes_number: int):
        (x,y) = divmod(minutes_number, 60)
        return '{}{},{}{}'.format(x, _('H'), y, _('M'))