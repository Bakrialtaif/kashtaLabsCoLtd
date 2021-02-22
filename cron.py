from django.conf import settings

from Core.models.Organization import Organization
from Core.models.DayInWeek import DayInWeek
from Core.models.Day import Day

from P010.control.SalesReports import SalesReports

import datetime

from Core.cons.HIERARCHY import list_of_organization_types

def my_cron_job():
    
    organization = Organization.objects.get(
            code=settings.GLOBAL_SETTINGS['ORGANIZATION_CODE'],
            type=list_of_organization_types().OWNER
            )

    day, created = Day.objects.get_or_create(
        organization=organization,
        day_in_week=DayInWeek.objects.get(value=3),
        date=datetime.date.today()
    )

    day.sales_number = SalesReports().get_day_sales_requests_number(date=datetime.date.today())
    day.revenue = SalesReports().get_day_revenue(date=datetime.date.today())
    day.profit = SalesReports().get_day_profit(date=datetime.date.today())
    day.save()