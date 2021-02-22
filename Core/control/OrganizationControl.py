from django.utils.translation import gettext_lazy as _
from django.utils import http
from django.http import HttpResponseRedirect
from django.contrib import messages

from Core.models.Organization import Organization
from Core.models.OrganizationUser import OrganizationUser
from Core.models.Component import Component
from Core.forms import OrganizationForm

from Core.cons.HIERARCHY import list_of_organization_types
from Core.cons.HIERARCHY import list_of_organization_user_types

class OrganizationCRUD():

    def __init__(self, request, organization: Organization, component_name: str):

        self.component = Component.objects.get(name=component_name)
        self.request = request
        self.organization = organization
        self.form = OrganizationForm(self.request.POST, instance=self.organization)

    def save(self, type: str):
        if self.request.method == "POST" and self.form.is_valid():

            organization = self.form.save()
            organization.component=self.component
            organization.type=type
            organization.save()
            
            try:
                OrganizationUser.objects.get_or_create(
                    organization=organization,
                    type=list_of_organization_user_types().CREATOR,
                    defaults={
                        'user': self.request.user
                    }
                )
            except OrganizationUser.MultipleObjectsReturned:
                pass
            messages.add_message(self.request, messages.SUCCESS, _('updated successfully'))
        else:
            messages.add_message(self.request, messages.SUCCESS, _('data is not correct'))

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
    
    def destroy(self):
        self.organization.delete()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))