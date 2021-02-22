from django.contrib.gis import forms as gis_form
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.forms.fields import CheckboxInput

from colorful.fields import RGBColorField
from leaflet.forms.widgets import LeafletWidget

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from Core.models.Organization import Organization
from Core.models.OrganizationUser import OrganizationUser
from Core.models.Place import Place
from Core.models.Document import Document
from Core.models.WF_Chart import WF_Chart
from Core.models.WF_Action import WF_Action
from Core.models.WF_Input import WF_Input
from Core.models.WF_Track import WF_Track
from Core.models.WF_Data import WF_Data
from Core.models.WF_Dump import WF_Dump
from Core.models.SheetParagraph import SheetParagraph
from Core.models.Component import Component
from Core.models.Paragraph import Paragraph
from Core.models.Parameter import Parameter
from Core.models.Permit import Permit
from Core.models.Feature import Feature
from Core.models.Procedure import Procedure
from Core.models.Sheet import Sheet
from Core.models.Element import Element
from Core.models.Fact import Fact
from Core.models.Datum import Datum
from Core.models.Analyze import Analyze
from Core.models.Version import Version
from Core.models.Refinement import Refinement
from P003.models.Unit import Unit
from P003.models.Vacant import Vacant

from Core.cons.WORKFLOW import list_of_executor_types
from Core.cons.WORKFLOW import list_of_input_choices
from Core.cons.WORKFLOW import list_of_action_types
from Core.cons.WORKFLOW import list_of_executions_status
from Core.cons.WORKFLOW import list_of_action_categories
from Core.cons.WORKFLOW import list_of_notification_types
from Core.cons.PRESENTATION import list_of_component_types
from Core.cons.GENERAL import list_of_notification_status
from Core.cons.TASK import list_of_task_types

class OrganizationForm(gis_form.ModelForm):
    class Meta:
        model = Organization
        fields = (
           'name',
           'phone',
           'email',
           'start_date',
           'title',
           'vision',
           'mission',
           'location',
        #    'geom',
        )
        widgets = {
            'location': LeafletWidget(),
            # 'geom': LeafletWidget(),
            'title': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
            'vision': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
            'mission': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            }

class OrganizationUserForm(forms.ModelForm):
    class Meta:
        model = OrganizationUser
        fields = (
           'user',
        )

class DocumentForm(forms.ModelForm):

    file = forms.FileField(required=True)

    class Meta:
        model = Document
        fields = (
            'name',
            'file',
            'description',
        )
        widgets = { 
            'description': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class DocumentUpdateForm(forms.ModelForm):    
    class Meta:
        model = Document
        fields = (
            'name',
            'description',
        )
        widgets = { 
            'description': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class WF_ChartForm(forms.ModelForm):    
    class Meta:
        model = WF_Chart
        fields = (
            'name',
            'order',
        )

class Wf_Action_First_Step_Form(forms.ModelForm):
    
    category = forms.ChoiceField(choices=list_of_action_categories().iteratable,label=_('category'), widget=forms.RadioSelect,required=True)

    class Meta:
        model = WF_Action
        fields = (
            'category',
            'order'
        )

class Wf_Action_Questionnaire_Form(forms.ModelForm):
    
    executor_type = forms.ChoiceField(choices=list_of_executor_types().iteratable,label=_('category'), widget=forms.RadioSelect,required=True)
    notification_type = forms.ChoiceField(choices=list_of_notification_types().iteratable,label=_('category'), widget=forms.RadioSelect,required=True)

    class Meta:
        model = WF_Action
        fields = (
            'name',
            'duration',
            'detail',
            'executor_type',
            'notification_type',
            'order'
        )
        widgets = { 
            'executor_type': forms.RadioSelect(),
            'notification_type': forms.RadioSelect(),
            'detail': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class Wf_Action_Procedure_Form(forms.ModelForm):
    
    executor_type = forms.ChoiceField(choices=list_of_executor_types().iteratable,label=_('category'), widget=forms.RadioSelect,required=True)
    notification_type = forms.ChoiceField(choices=list_of_notification_types().iteratable,label=_('category'), widget=forms.RadioSelect,required=True)

    class Meta:
        model = WF_Action
        fields = (
            'procedure',
            'duration',
            'detail',
            'executor_type',
            'notification_type',
            'order'
        )
        widgets = { 
            'executor_type': forms.RadioSelect(),
            'notification_type': forms.RadioSelect(),
            'detail': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

    def __init__(self, chart_id, *args, **kwargs):
        self.instance = kwargs.get('instance', None)
        super(Wf_Action_Procedure_Form, self).__init__(*args, **kwargs)
        self.fields['procedure'] = forms.ModelChoiceField(
            queryset=Procedure.objects.filter(component=WF_Chart.objects.get(pk=chart_id).component,support_workflow=True).all(),
            label=_('procedure'),
            widget=forms.RadioSelect,
            empty_label=None,
            required=True)

class WF_InputForm(forms.ModelForm):
    class Meta:
        model = WF_Input
        fields = (
            'title',
            'type',
            'required',
            'default',
            'order',
            'help',
        )
        widgets = {
            'required' : CheckboxInput(attrs={'class': 'required checkbox'}),
            'help': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class WF_TrackForm(forms.ModelForm):
    class Meta:
        model = WF_Track
        fields = (
            'name',
            'order',
        )
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'required'}),
        }        

class WF_XForm(forms.Form):
    
    def __init__(self, request, action_id, *args, **kwargs):
        super(WF_XForm, self).__init__(*args, **kwargs)

        inputs = WF_Input.objects.filter(action_id=action_id).all()

        for input in inputs:

            list_inputs = []
            attributes = None

            if input.type == list_of_input_choices().MODELCHOICEFIELD:
                list_inputs.append("queryset=%s" % ('input.tracks.all()'))

            if input.title:

                if input.required:
                    list_inputs.append('label="%s (*)"' % (input.title))
                    list_inputs.append("required='required'")
                else:
                    list_inputs.append('label="%s "' % (input.title))
                    list_inputs.append("required=False")
            
            if input.type == list_of_input_choices().TEXTAREAFIELD:
                input.type = list_of_input_choices().CHARFIELD
                list_inputs.append("widget=forms.Textarea(attrs={'width':'100%'})")
            
            if input.help:
                list_inputs.append("help_text='%s'" % (input.help))

            if input.default:
                list_inputs.append("initial='%s'" % (input.default))


            try:
                self.fields["id_%s" % (input.pk)] = eval("forms.%s( %s )" % (input.type, ','.join(map(str, list_inputs))))
            except SyntaxError or TypeError:
                messages.add_message(request, messages.ERROR, ( '%s : %s' % (_('review your field : '), input.title)))


class WF_TaskForm(forms.Form):
    
    def __init__(self, request, requestObject, action_id, *args, **kwargs):
        super(WF_TaskForm, self).__init__(*args, **kwargs)

        initial_values = dict(WF_Data.objects.filter(
            request=requestObject,
            action=requestObject.action,
            task=requestObject.task
        ).values_list('input_id', 'value'))

        inputs = WF_Input.objects.filter(action_id=action_id).all()
        for input in inputs:

            list_inputs = []
            attributes = None

            if input.type == list_of_input_choices().MODELCHOICEFIELD:
                list_inputs.append("queryset=%s" % ('input.tracks.all()'))

            if input.title:

                if input.required:
                    list_inputs.append('label="%s (*)"' % (input.title))
                    list_inputs.append("required='required'")
                else:
                    list_inputs.append('label="%s "' % (input.title))
                    list_inputs.append("required=False")
            
            if input.type == list_of_input_choices().TEXTAREAFIELD:
                input.type = list_of_input_choices().CHARFIELD
                list_inputs.append("widget=forms.Textarea(attrs={'width':'100%'})")
            
            if input.help:
                list_inputs.append("help_text='%s'" % (input.help))

            if input.default:
                pass
                # list_inputs.append("initial='%s'" % ( initial_values[input.pk] if initial_values[input.pk] else input.default ))

            try:
                self.fields["id_%s" % (input.pk)] = eval("forms.%s( %s )" % (input.type, ','.join(map(str, list_inputs))))
                try:
                    self.fields["id_%s" % (input.pk)].initial = input.default if initial_values[input.pk] == None else initial_values[input.pk]
                    # if input.type == list_of_input_choices().MODELCHOICEFIELD:
                    #     self.fields["id_%s" % (input.pk)].initial = input.default if input.data.first().track.pk == None else input.data.first().track.pk
                    # else:
                except KeyError:
                    pass
            except SyntaxError or TypeError:
                messages.add_message(request, messages.ERROR, ( '%s : %s' % (_('review your field : '), input.title)))

        try:
            self.fields['execution_status'] = forms.ChoiceField(
                choices=list_of_executions_status().iteratable,
                label=_('execution status'),
                widget=forms.RadioSelect,
                required=True,
                initial=requestObject.task.execution_status
                )
        except:
            pass

class WF_ActionExecutorForm(forms.Form):

    executor = forms.IntegerField()
    action = None
    vacants = None

    def __init__(self, action, *args, **kwargs):
        super(WF_ActionExecutorForm, self).__init__(*args, **kwargs)
        self.action = action

        if action.executor_type == list_of_executor_types.SPECIFIC_EMPLOYEE:                
            self.vacants = [(vacant.user.pk, vacant) for vacant in Vacant.objects.getOrganizationEmployees()]

        if action.executor_type == list_of_executor_types.ANY_UNIT_MANAGER:
            self.vacants = [(unit.manager.id, '%s >> %s' % (unit.manager.get_full_name(), unit.name)) for unit in Unit.objects.getUnits().all() if unit.manager]

        if action.executor_type == list_of_executor_types.FROM_RECORD:
            self.vacants = Vacant.objects.getOrganizationEmployees()

        # if self.vacants:
        self.fields['executor'] = forms.ChoiceField(choices=self.vacants,label=_('specify action user executor'),widget=forms.RadioSelect,required=True)

    def save(self, commit=True):
        if commit:
            self.action.executor = User.objects.get(pk=self.data['executor'])
            self.action.save()

class WF_DumpForm(forms.ModelForm):    
    class Meta:
        model = WF_Dump
        fields = (
            'name',
            'justifications',
        )
        widgets = {
            'justifications': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class SheetForm(forms.ModelForm):    
    class Meta:
        model = Sheet
        fields = (
            'code',
            'description',
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class SheetParagraphForm(forms.ModelForm):    
    class Meta:
        model = Paragraph
        fields = (
            'title',
            'body',
        )
        widgets = {
            'body': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class PackageForm(forms.ModelForm):    
    class Meta:
        model = Component
        fields = (
            'name',
            'about',
            'show_in_menu',
            'order',
        )
        widgets = {
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class ProgramForm(forms.ModelForm):    
    class Meta:
        model = Component
        fields = (
            'parent',
            'name',
            'about',
            'show_in_menu',
            'order',
            'url',
        )
        widgets = {
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class MenuForm(forms.ModelForm):    
    class Meta:
        model = Component
        fields = (
            'parent',
            'name',
            'about',
            'show_in_menu',
            'order',
        )
        widgets = {
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class OperationForm(forms.ModelForm):

    class Meta:
        model = Component
        fields = (
            'parent',
            'name',
            'url',
            'color',
            'about',
            'content_type',
            'show_in_menu',
            'show_in_permissions',
            'support_workflow',
            'support_documents',
            'document_ownership',
            'order',
        )
        widgets = {
            'url' : forms.TextInput(attrs={'class': 'required'}),
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class ParameterForm(forms.ModelForm):    
    class Meta:
        model = Parameter
        fields = (
            'name',
            'value',
            'order',
        )

class PermitForm(forms.ModelForm):    
    class Meta:
        model = Permit
        fields = (
            'code',
            'order',
        )        

class FeatureForm(forms.ModelForm):    
    class Meta:
        model = Feature
        fields = (
            'title',
            'body',
            'order',
        )
        widgets = {
            'body': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class ProcedureForm(forms.ModelForm):

    class Meta:
        model = Procedure
        fields = (
            'code',
            'support_workflow',
            'order',
        )        

class ParagraphForm(forms.ModelForm):    
    class Meta:
        model = Paragraph
        fields = (
            'type',
            'title',
            'body',
            'order',
        )
        widgets = {
            'body': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class ContextForm(forms.ModelForm):    
    class Meta:
        model = Element
        fields = (
            'code',
            'about',
            'order',
        )
        widgets = {
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class CaseForm(forms.ModelForm):    
    class Meta:
        model = Element
        fields = (
            'code',
            'about',
            'order',
        )
        widgets = {
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class FactForm(forms.ModelForm):    
    class Meta:
        model = Fact
        fields = (
            'code',
            'about',
            'order',
        )
        widgets = {
            'about': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class DatumForm(forms.ModelForm):    
    class Meta:
        model = Datum
        fields = (
            'code',
            'type',
            'translatable',
            'order'
        )

class AnalyzeForm(forms.ModelForm):    
    class Meta:
        model = Analyze
        fields = (
            'code',
            'type',
            'periodicity',
            'purposes',
            'order',
        )
        widgets = {
            'purposes': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
        }

class AlertsSpecificationsFiltersForm(forms.Form):
    
    status = forms.MultipleChoiceField(label=_('status'), choices=list_of_notification_status().iteratable, widget=forms.CheckboxSelectMultiple, required=False)
    type = forms.MultipleChoiceField(label=_('type'), choices=list_of_task_types().iteratable, widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        pass

class StateForm(gis_form.ModelForm):
    class Meta:
        model = Place
        fields = (
            'name',
            'location',
            'geom',
            'order',
        )
        widgets = {
            'location': LeafletWidget(),
            'geom': LeafletWidget(),
            }

class ProvinceForm(gis_form.ModelForm):
    class Meta:
        model = Place
        fields = (
            'name',
            'location',
            'geom',
            'order',
        )
        widgets = {
            'location': LeafletWidget(),
            'geom': LeafletWidget(),
            }

class TownForm(gis_form.ModelForm):
    class Meta:
        model = Place
        fields = (
            'name',
            'location',
            'geom',
            'order',
        )
        widgets = {
            'location': LeafletWidget(),
            'geom': LeafletWidget(),
            }

class DistrictForm(gis_form.ModelForm):
    class Meta:
        model = Place
        fields = (
            'name',
            'location',
            'geom',
            'order',
        )
        widgets = {
            'location': LeafletWidget(),
            'geom': LeafletWidget(),
            }

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = (
            'name',
            'description',
            'start_date',
            'end_date',
            'order',
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker'}),
            }

class RefinementForm(forms.ModelForm):
    class Meta:
        model = Refinement
        fields = (
            'version',
            # 'component',
            'name',
            'description',
            'start_date',
            'end_date',
            'status',
            'order',
        )
        widgets = {
            'description': forms.Textarea(attrs={'rows':3, 'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker'}),
            }

