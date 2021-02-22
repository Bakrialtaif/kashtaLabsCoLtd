from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.contrib.auth.models import User
from P001.models.Profile import Profile
from P001.models.Education import Education
from P001.models.Training import Training
from P001.models.Work import Work

from P011.models.Year import Year
from P011.models.ProfileYear import ProfileYear

from Core.cons.TASK import list_of_task_types
from Core.cons.TASK import list_of_priority_types
from Core.cons.TASK import list_of_executions_status
from Core.cons.TASK import list_of_completion_status

from Core.cons.GENERAL import list_of_app_labels
from P011.cons.FISCAL import list_of_fiscal_year_openness_status

from Core.cons.PROFILE import list_of_health_status

class basicDataForm(forms.ModelForm):

    username = forms.CharField(validators=[UnicodeUsernameValidator])

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
        )
        widgets = {
            'first_name' : forms.TextInput(attrs={ 'required': 'true' }),
            'last_name' : forms.TextInput(attrs={ 'required': 'true' }),
            'email' : forms.EmailInput(attrs={ 'required': 'true' }),
        
        }

class contactDataForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = (
            'phone',
            'facebook',
            'twitter',
            'title',
        )
        widgets = {
            'title': forms.Textarea(attrs={'rows': 3, 'class':'form-control'})
        }

class personalDataForm(forms.ModelForm):

    health_status = forms.MultipleChoiceField(choices=list_of_health_status().iteratable, widget=forms.CheckboxSelectMultiple(), validators=[])
    
    class Meta:
        model = Profile
        fields = (
            'sex',
            'nationality',
            'birthdate',
            'martial_status',
            'work_status',
            'health_status',
        )
        widgets = {
            'birthdate': forms.DateInput(attrs={'class':'datepicker'}),
        }

    def is_valid(self):
        valid = super(personalDataForm, self).is_valid()
 
        # if not valid:
        #     return valid
 
class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = (
            'degree',
            'date',
            'Specialization',
            'institution',
        )
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'})
        }

class WorkForm(forms.ModelForm):
    
    class Meta:
        model = Work
        fields = (
            'company',
            'title',
            'start_date',
            'end_date',
            'current'
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker'})
        }

class TrainingForm(forms.ModelForm):
    
    class Meta:
        model = Training
        fields = (
            'institute',
            'title',
            'start_date',
            'end_date',
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker'})
        }

class TaskFiltersForm(forms.Form):

    type = forms.MultipleChoiceField(label=_('task type'), choices=list_of_task_types().iteratable, widget=forms.CheckboxSelectMultiple, required=False)
    priority = forms.MultipleChoiceField(label=_('priority'), choices=list_of_priority_types().iteratable, widget=forms.CheckboxSelectMultiple, required=False)
    execution = forms.MultipleChoiceField(label=_('execution status'), choices=list_of_executions_status().iteratable, widget=forms.CheckboxSelectMultiple, required=False)
    completion = forms.MultipleChoiceField(label=_('completion status'), choices=list_of_completion_status().iteratable, widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        pass

class UserSpecificationForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = []