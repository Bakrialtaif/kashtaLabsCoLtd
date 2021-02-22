from django.urls import path
from P000.views import home

app_name = 'P000'

urlpatterns = [

    path('', home.show, name='website-home'),
    path('login-request/', home.login_request, name='login-request'),
    path('logout/', home.logout_user, name='logout'),
]