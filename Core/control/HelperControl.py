from django.utils.translation import gettext_lazy as _

import os
import sys
import datetime
from django.core.management import call_command
from django.conf import settings


from django.contrib.contenttypes.models import ContentType

from Core.models.Component import Component
from Core.models.Paragraph import Paragraph
from Core.models.Permit import Permit
from Core.models.Procedure import Procedure
from Core.models.Day import Day
from Core.models.DayInWeek import DayInWeek

from django.contrib.auth.models import User
from Core.models.Organization import Organization
from Core.models.Place import Place
from Core.models.Sheet import Sheet
from Core.models.Element import Element
from P001.models.Profile import Profile
from P003.models.Folder import Folder
from P007.models.Item import Item
from P011.models.Account import Account

from Core.cons.GENERAL import list_of_app_labels
from Core.cons.GENERAL import list_of_model_names

from Core.cons.INVENTORY import list_of_item_types
from P011.cons.FISCAL import list_of_account_types
from P011.cons.FISCAL import list_of_nature_types

from Core.cons.ARCHIVE import list_of_folder_types
from Core.cons.ARCHIVE import list_of_box_types

from Core.cons.HIERARCHY import list_of_organization_types
from Core.cons.PRESENTATION import list_of_component_types
from Core.cons.REPORT import list_of_element_types
from Core.cons.REPORT import list_of_dimension_types
from Core.cons.GENERAL import list_of_component_names
from Core.cons.GENERAL import list_of_place_types
from Core.cons.GENERAL import list_of_week_days

# Education 
from Core.models.UserClassification import UserClassification

from Core.cons.BLADALNOOR import list_of_user_classification_types

class browse_Model_Data():

    def __init__(self, modelObject):
        self.model_object = modelObject
        self.model_name = str(self.model_object.__class__.__name__).lower()
        self.model_browsable_data()

    def get_form(self):
        return dict((name, self.get_value(name)) for name in self.browsable_data)

    def get_value(self, name):

        value = getattr(self.model_object, name)

        if name in ['user', 'created_by','sended_by','assigned_by','assigned_to']:
            try:
                return value.get_full_name()
            except:
                return value

        elif name in self.translatable_data:
            return _(value)

        else:
            return value
    
    def model_browsable_data(self):

        if self.model_name == list_of_model_names().PERMISSION:
            self.browsable_data = ['user','vacant','date','start_time','end_time','justifications','created_by','created_at','updated_at']
            self.translatable_data = []
        
        elif self.model_name == list_of_model_names().WF_DUMP:
            self.browsable_data = ['user','name','justifications','created_by','created_at','updated_at']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().PROFILE:
            self.browsable_data = ['user','title','birthdate','phone','facebook','twitter']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().ORGANIZATION:
            self.browsable_data = ['name','phone','email','title']
            self.translatable_data = []
        
        elif self.model_name == list_of_model_names().WF_REQUEST:
            self.browsable_data = ['user','status','action','success','created_by','sended_by','created_at','updated_at','sended_at','finish_at']
            self.translatable_data = ['status']

        elif self.model_name == list_of_model_names().PROJECT:
            self.browsable_data = ['unit','name','start_date','end_date','assumptions','scope_include','scope_exclude','manager','order']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().TASK:
            self.browsable_data = ['priority','assigned_by','assigned_to','assigned_date','start_date','duration','end_date','execution_status','execution_date']
            self.translatable_data = ['priority', 'execution_status']

        elif self.model_name == list_of_model_names().OPERATIONAL_PLAN:
            self.browsable_data = ['business_model','name','start_date','end_date','created_by']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().TRANSACTION:
            self.browsable_data = ['topic','content','language','date','created_by','created_at','updated_at']
            self.translatable_data = ['language']

        elif self.model_name == list_of_model_names().PARAGRAPH:
            self.browsable_data = ['type','title','body','order']
            self.translatable_data = ['type']
            
        elif self.model_name == list_of_model_names().COMPONENT:
            self.browsable_data = ['name','type','about','icon','order']
            self.translatable_data = ['type']

        elif self.model_name == list_of_model_names().FLEET:
            self.browsable_data = ['type','purpose','trademark','model','chassis_number','engin_number','engin_capacity','created_by','created_at','updated_at']
            self.translatable_data = ['type','purpose']

        elif self.model_name == list_of_model_names().UNIT:
            self.browsable_data = ['type','parent','building','manager','name','descriptions','order','created_at','updated_at']
            self.translatable_data = ['type']

        elif self.model_name == list_of_model_names().CARD:
            self.browsable_data = ['unit','name','type','descriptions','direct_boss','responsible_to','in_charge_of','conditions','order']
            self.translatable_data = ['type']
            
        elif self.model_name == list_of_model_names().BUSINESSMODEL:
            self.browsable_data = ['name', 'description']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().VOUCHER:
            self.browsable_data = ['year','user','type','status','serial','vender','created_by','created_at','updated_at']
            self.translatable_data = []
        
        elif self.model_name == list_of_model_names().EDUCATION:
            self.browsable_data = ['user','degree','date','Specialization','institution','created_at','updated_at']
            self.translatable_data = ['degree']

        elif self.model_name == list_of_model_names().WORK:
            self.browsable_data = ['user','company','title','start_date','end_date','current','created_at','updated_at']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().TRAINING:
            self.browsable_data = ['user','institute','title','start_date','end_date','created_at','updated_at']
            self.translatable_data = []

        elif self.model_name == list_of_model_names().Item:
            self.browsable_data = ['name', 'about', 'unit']
            self.translatable_data = []

        else:
            self.browsable_data = []
            self.translatable_data = []

class PreparationBasicConfiguration():

    def __init__(self):
        self.organization = None
        self.loaddata()
        self.update_owner_organization_data()
        self.days_in_week_preparation()
        self.create_start_day_for_log()
        self.update_super_user_profile()
        self.update_basic_documents_operation()
        self.sheets_update()
        self.archive_boxes_preparation()
        self.reports_first_element_preparation()
        self.inventory_pre_preparation()
        self.places_pre_preparation()
        self.user_classify_in_education()

    def loaddata(self):
    
        print('[1] Loading structural data ...')

        orderedListOfFiles = [
            '%s/dump-data/Core/component.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/paragraph.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/feature.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/parameter.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/permit.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/procedure.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/version.json' % (settings.BASE_DIR),
            '%s/dump-data/Core/refinement.json' % (settings.BASE_DIR),
            '%s/dump-data/P002/quote.json' % (settings.BASE_DIR),
        ]

        for file in orderedListOfFiles:
            call_command('loaddata',file)

    def update_owner_organization_data(self):
        self.organization, created = Organization.objects.update_or_create(
                code=settings.GLOBAL_SETTINGS['ORGANIZATION_CODE'],
                type=list_of_organization_types().OWNER,
                defaults={
                    'component': Component.objects.get(name=list_of_component_names().organization),
                    'programs':','.join(map(str, [
                    'P002',
                    'P003',
                    'P004',
                    'P005',
                    'P006',
                    'P007',
                    'P008',
                    'P009',
                    'P010',
                    'P011',
                    'P012',
                    'P013',
                    'P016',
                    'P017',
                    'P018',
                    'P019',
                    'Reports'
                    ])),
                    'start_date': settings.SYSTEM_START_DATE,
                    })
        print('[2] organization existens and it data updated successfully ...')

    def days_in_week_preparation(self):
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Monday, value=0)
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Tuesday, value=1)
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Wednesday, value=2)
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Thursday, value=3)
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Friday, value=4)
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Saturday, value=5)
        DayInWeek.objects.update_or_create(organization=self.organization, name=list_of_week_days().Sunday, value=6)
        print('[3] Days in week updated successfully ...')

    def create_start_day_for_log(self):
        start_date = datetime.datetime.strptime(settings.SYSTEM_START_DATE, "%Y-%m-%d").date()
        self.organization.days.update_or_create(
                    date=start_date,
                    day_in_week=DayInWeek.objects.get(value=start_date.weekday())
                )
        print('[4] organization start date log record created successfully ...')

    def update_super_user_profile(self):
        superusers = User.objects.filter(is_superuser=True)
        for superuser in superusers:
            try:
                superuser.profile.component=Component.objects.get(name=list_of_component_names().profile)
                superuser.profile.save()
            except Profile.DoesNotExist:
                Profile.objects.create(component=Component.objects.get(name=list_of_component_names().profile),user=superuser)
        print('[5] Superuser profile updated successfully ...')

    def update_basic_documents_operation(self):
        Component.objects._mptt_filter(name=list_of_component_names().organization).update(support_documents=True, permitted_doc_no=1)
        Component.objects._mptt_filter(name=list_of_component_names().profile).update(support_documents=True, permitted_doc_no=1)
        Component.objects._mptt_filter(name=list_of_component_names().permission_request).update(support_documents=True, permitted_doc_no=1)
        Component.objects._mptt_filter(name=list_of_component_names().dump_requests).update(support_documents=True, permitted_doc_no=1)
        Component.objects._mptt_filter(name=list_of_component_names().operational_plans).update(support_documents=True, permitted_doc_no=1)
        Component.objects._mptt_filter(name=list_of_component_names().entries).update(support_documents=True, permitted_doc_no=1)
        Component.objects._mptt_filter(name=list_of_component_names().purchases).update(support_documents=True, permitted_doc_no=1)
        print('[6] Operations with document updated successfully ...')
    
    def sheets_update(self):
        sheet_list = settings.GLOBAL_SETTINGS['SHEET_LIST']
        for app in sheet_list:
            app_label = app[0]
            sheets = app[1]
            for sheet in sheets:
                Sheet.objects.get_or_create(app_label=app_label, code=sheet[0])
        print('[7] Sheets updated successfully ...')


    def archive_boxes_preparation(self):

        Folder.objects.update_or_create(
            user=None,
            type=list_of_folder_types().ORGANIZATION_INBOX,
            name=list_of_box_types().INBOX,
            defaults={
                'about':'ORGANIZATION INBOX DESCRIPTION',
                'order':1,
                }
        )

        Folder.objects.update_or_create(
            user=None,
            type=list_of_folder_types().ORGANIZATION_OUTBOX,
            name=list_of_box_types().OUTBOX,
            defaults={
                'about':'ORGANIZATION OUTBOX DESCRIPTION',
                'order':2,
                }
        )

        print('[8] Archives folders updated successfully ...')

    def reports_first_element_preparation(self):

        top_element, status = Element.objects.update_or_create(
            parent=None,
            type=list_of_element_types().START,
            order=0,
            defaults={
                'code':'reports',
                'about':'0',
            }
        )

        Element.objects.update_or_create(
            code=list_of_dimension_types.ORGANIZATIONAL,
            type=list_of_element_types().DIMENSION,
            order=1,
            defaults={
                'parent':top_element,
                'about':'1',
            }
        )

        Element.objects.update_or_create(
            code=list_of_dimension_types.OPERATIONAL,
            type=list_of_element_types().DIMENSION,
            order=2,
            defaults={
                'parent':top_element,
                'about':'2',
            }
        )

        Element.objects.update_or_create(
            code=list_of_dimension_types.FINANCIAL,
            type=list_of_element_types().DIMENSION,
            order=3,
            defaults={
                'parent':top_element,
                'about':'3',
            }
        )

        Element.objects.update_or_create(
            code=list_of_dimension_types.CUSTOMERS,
            type=list_of_element_types().DIMENSION,
            order=4,
            defaults={
                'parent':top_element,
                'about':'4',
            }
        )

        Element.objects.update_or_create(
            code=list_of_dimension_types.LEARNING,
            type=list_of_element_types().DIMENSION,
            order=5,
            defaults={
                'parent':top_element,
                'about':'5',
            }
        )

        Element.objects.update_or_create(
            code=list_of_dimension_types.GROWTH,
            type=list_of_element_types().DIMENSION,
            order=6,
            defaults={
                'parent':top_element,
                'about':'6',
            }
        )

        print('[9] Reports dimensions updated successfully ...')

    def inventory_pre_preparation(self):

        Item.objects.update_or_create(
            parent=None,
            serial=0,
            order=0,
            type=list_of_item_types().CATEGORY,
            defaults={
                'organization':self.organization,
                'name':_('inventory'),
                'about':'',
                'code':'',
                'activation':True,
                'indent':'',
            }
        )

        print('[10] Inventory updated successfully ...')

    def places_pre_preparation(self):
    
        Place.objects.update_or_create(
            parent=None,
            type=list_of_place_types().COUNTRY,
            order=0,
            defaults={
                'name': 'country',
                'color': '#333',
                'indent': '',
                'location': None,
                'geom': None
            }
        )

        print('[11] Places first element updated successfully ...')

    def user_classify_in_education(self):

        # General
        UserClassification.objects.update_or_create(organization=self.organization, name=list_of_user_classification_types().EMPLOYEE, order=1)
        UserClassification.objects.update_or_create(organization=self.organization, name=list_of_user_classification_types().CLIENT, order=2)

        print('[12] User classifies in education ...')