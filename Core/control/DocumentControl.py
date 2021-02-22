from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from Core.models.Component import Component
from Core.models.Organization import Organization
from Core.models.Task import Task
from Core.models.WF_Dump import WF_Dump
from Core.models.Document import Document
from P003.models.Permission import Permission
from P001.models.Profile import Profile
from P001.models.Education import Education
from P001.models.Work import Work
from P001.models.Training import Training
from P013.models.OperationalPlan import OperationalPlan
from P003.models.Transaction import Transaction
from P011.models.Voucher import Voucher
from P007.models.Item import Item

from Core.forms import DocumentForm
from Core.forms import DocumentUpdateForm

from Core.cons.GENERAL import list_of_app_labels
from Core.cons.GENERAL import list_of_model_names
from Core.cons.GENERAL import list_of_ownership_types
from Core.cons.GENERAL import list_of_component_names

class DocumentControl:

    def __init__(self,model_class: str, model_id: int, component_name: str):

        self.object = self.get_model_object(model_class=model_class, model_id=model_id)
        self.component = self.object.component
        self.documents = self.object.documents.filter(component=Component.objects.get(name=component_name)).all()

    def get_model_object(self, model_class, model_id):
        return eval('%s.objects.get(pk=%s)' % (model_class, model_id))

    def get_document_data(self):

        return {
                'object': self.object,
                'documents': self.documents,
                'component': self.component,
                'permitted_doc_no': self.component.permitted_doc_no - self.documents.count()
            }
    
    def create_document(self,request):

        if request.method == "POST":

            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():

                document = form.save(commit=False);
                document.component=self.component
                document.user=request.user
                document.name=form.cleaned_data['name']
                document.description=form.cleaned_data['description']
                document.extension=request.FILES['file'].content_type
                document.size=request.FILES['file'].size
                document.created_by=request.user

                document.organization = self.object if self.component.name in [list_of_component_names().organization, list_of_component_names().customers, list_of_component_names().suppliers] else request.organization
                document.permission = self.object if self.component.name == list_of_component_names().permission_request else None
                document.task = self.object if self.component.name == list_of_component_names().tasks else None
                document.wf_dump = self.object if self.component.name == list_of_component_names().dump_requests else None
                document.profile = self.object if self.component.name == list_of_component_names().profile else None
                document.education = self.object if self.component.name == list_of_component_names().education_data else None
                document.work = self.object if self.component.name == list_of_component_names().work_data else None
                document.training = self.object if self.component.name == list_of_component_names().training_data else None
                document.operational_plan = self.object if self.component.name == list_of_component_names().operational_plans else None
                document.transaction = self.object if self.component.name == list_of_component_names().archives_transactions else None
                document.voucher = self.object if self.component.name == list_of_component_names().purchases else None
                document.item = self.object if self.component.name == list_of_component_names().inventory_categories_and_items else None

                document.save()

                return True, []

            else:

                return False, form.errors


    def update_document(self, request, document_id):        
        form = DocumentUpdateForm(request.POST, request.FILES, instance=Document.objects.get(id=document_id))
        if form.is_valid():  
            form.save()
            return True, []
        else:
            return False, form.errors

    def delete_document(self, document_id):
        result = Document.objects.get(id=document_id).delete()
        if result[0] == 1:
            return True
        else:
            return False