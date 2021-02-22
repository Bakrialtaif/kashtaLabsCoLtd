from django.db import models
from django.utils.translation import gettext_lazy as _

class ProcedureABC:

    def get_path(self, back_url):
        raise Exception('you should build get_path() function inside your procedure.')

    def procedure_start_process(self):
        raise Exception('you should build procedure_start_process() function inside your procedure.')

    def procedure_end_process(self):
        raise Exception('you should build procedure_end_process() function inside your procedure.')

    def status(self):
        raise Exception('you should build status() function inside your procedure.')

    def failures(self):
        raise Exception('you should build failures() function inside your procedure.')