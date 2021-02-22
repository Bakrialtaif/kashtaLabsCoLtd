from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils import http
from django.http import HttpResponseRedirect

from Core.models.UserPermit import UserPermit

def have_a_permit(permit=None):
    def decorator(function):
        def wrap(request, *args, **kwargs):
            if permit in request.user.profile.get_permits:
                return function(request, *args, **kwargs)
            else:
                messages.add_message(request, messages.ERROR, _('you have not permission to visit this operation'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
        return wrap
    return decorator


def profile_has_active_fiscal_year(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.active_year:
            return function(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR, _('you should activate user fiscal year first'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
    return wrap

def organization_has_active_fiscal_year(function):
    def wrap(request, *args, **kwargs):
        if request.organization.active_year:
            return function(request, *args, **kwargs)
        else:
            messages.add_message(request, messages.ERROR, _('you should activate vouchers fiscal year first'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  
    return wrap
