from django.utils.translation import gettext_lazy as _

import os
from django.core.management import call_command
from django.conf import settings


from django.contrib.contenttypes.models import ContentType

from Core.models.Component import Component
from Core.models.Paragraph import Paragraph
from Core.models.Permit import Permit
from Core.models.Procedure import Procedure
from Core.models.DayInWeek import DayInWeek

from Core.cons.GENERAL import list_of_app_labels
from Core.cons.GENERAL import list_of_model_names

from Core.models.Element import Element
from P007.models.Item import Item


class DatabaseController():
    
    def save_db_to_file(self, content: ContentType):
        filename = '%s/dump-data/%s/%s.json' % (settings.BASE_DIR, content.app_label, content.model)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        output = open(filename,'w+')
        call_command(
            'dumpdata',
            '%s.%s' % (content.app_label,
            content.model),
            format='json',
            indent=4,
            stdout=output)
        output.close()

    def save_component_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().COMPONENT))

    def save_feature_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().FEATURE))

    def save_parameter_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().PARAMETER))

    def save_permit_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().PERMIT))

    def save_paragraph_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().PARAGRAPH))

    def save_element_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().ELEMENT))

    def save_fact_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().FACT))

    def save_datum_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().DATUM))

    def save_analyze_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().ANALYZE))

    def save_procedures_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().PROCEDURE))

    def save_versions_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().VERSION))

    def save_refinements_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().CORE, model=list_of_model_names().REFINEMENT))

    def save_quotes_to_file(self):
        self.save_db_to_file(content=ContentType.objects.get(app_label=list_of_app_labels().P002, model=list_of_model_names().QUOTE))

    def prepare_db_ideoms_to_in_translation_file(self):

        list_of_model_columns = [
                    ('Component','name'),
                    ('Paragraph','title'),
                    ('Permit','code'),
                    ('Procedure','code'),
                    ('DayInWeek','name'),
                    ]

        for item in list_of_model_columns:
            filename = '%s/trans/%s/%s.py' % (settings.BASE_DIR, item[0], item[1])
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            output = open(filename,'w+')
            for row in eval('%s.objects.all()' % (item[0])):
                output.write("_('%s')\n" % (eval('row.%s' % (item[1]))))
                if item[0] == 'Procedure':
                    output.write("_('%s_description')\n" % (eval('row.%s' % (item[1]))))
            output.close()