from django.urls import path
from P001.views import home

app_name = 'P001'

urlpatterns = [
    path('', home.show, name='home'),
]