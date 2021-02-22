from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import translation
from django.shortcuts import redirect
from django.conf import settings
from django.utils import http
from django.http import HttpResponseRedirect

@login_required
def home(request):

    context = {
    }

    return render(request, 'P001_kashta/home.html', context=context)