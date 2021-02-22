from django.urls import path
from P001.views import home, kashta, bladalnoor, batinjan

app_name = 'P001'

urlpatterns = [
    path('', home.show, name='home'),
    path('kashta/home', kashta.home, name='kashta-home'),
    path('bladalnoor/home', bladalnoor.home, name='bladalnoor-home'),
    path('batinjan/home', batinjan.home, name='batinjan-home'),
]