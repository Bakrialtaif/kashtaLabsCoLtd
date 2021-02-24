"""
Django settings for system project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _
import django_heroku
import dj_database_url

from Core.cons.GENERAL import list_of_countries_names

SYSTEM_NAME = 'Blad Al-Noor E-Market'
ORGANIZATION_NAME = 'ORGANIZATION_NAME'
ORGANIZATION_CODE = 'ORGANIZATION_CODE'
ORGANIZATION_COUNTRY = list_of_countries_names().SDN
SYSTEM_START_DATE = '2021-01-01'

################################################################################
################################################################################
################################################################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^jt*8mb=9!h2%6z@r6&x-au=-hr-d2738%$s!ivl@7haw!-+m@'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'bladalnoor.com', '142.93.153.198']
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Allauth 
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Social login
    'allauth.socialaccount.providers.github',

    # apps
    'Core',
    'P000',
    'P001',

    # gis
    'django.contrib.gis',
    'djgeojson',
    # 'leaflet',
    # 'colorful',

    # helpers
    'django_cleanup',
    'django_extensions',
    "bidiutils",
    'languages',

    # api
    # 'rest_framework',

    # ckeditor
    # 'ckeditor',

    # 'django_crontab',
]

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
}

MIDDLEWARE = [
    'system.middleware.basicMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',

    # Custom Middleware 
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bidiutils.context_processors.bidi',
            ],
            'libraries': {
                'general_tags': 'system.custom_tags.general_tags',
            },
        },
    },
]

WSGI_APPLICATION = 'system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',
    #     'NAME': 'ba',
    #     'USER': 'postgres',
    #     'PASSWORD': '123456',
    #     'HOST': 'localhost',
    #     'PORT': '5432',
    # },
}

# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ar'
LANGUAGES = (
    ('ar', _('Arabic')),
    ('en', _('English')),
)

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/') 
MEDIA_URL = '/uploads/'

# Email settings
 
SERVER_EMAIL = 'altaif.bakri@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = SERVER_EMAIL
EMAIL_HOST_PASSWORD = '*********'



ADMINS = [
    ('BakriAltaif', 'altaif.bakri@gmail.com'),
]

# General Settings 
MANAGERS = ADMINS
LOGIN_URL = '/'
LOGOUT_REDIRECT_URL = '/'
AUTH_PROFILE_MODULE = 'dashboard_app.Profile'

LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (21.5, 22.5, 38.5, 8.5),
    'DEFAULT_CENTER': (13.1,30.2),
    'DEFAULT_ZOOM': 8,
    'MIN_ZOOM': 1,
    'MAX_ZOOM': 20,
    'TILES': [
        (
        'مخطط', 
        'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png', {
            'attribution': '', 
            }
        ),
        (
        'قمر صناعي',
        'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	        'attribution': '',
            }
        )
        ],
    'ATTRIBUTION_PREFIX': '&copy; <a href="/" target="_blank">Kashta ELP</a>',
    'SCALE': 'both',
    # 'MINIMAP': True,
    }

API_URI = 'http://127.0.0.1:8000'
# *********************************************************************************************************************

YES = 'YES'
NO = 'NO'

WORKING = 'WORKING'
NOTWORKING = 'NOTWORKING'

NO_MAINTENANCE = 'NO_MAINTENANCE'
MAINTENANCE = 'MAINTENANCE'
TO_GET_RIDE = 'TO_GET_RIDE'

USED = 'USED'
IDLE = 'IDLE'

BASIC = 'BASIC'
SECONDARY = 'SECONDARY'

BUSY = 'BUSY'
NOT_BUSY = 'NOT_BUSY'

ACTIVATED = 'ACTIVATED'
NOT_ACTIVATED = 'NOT_ACTIVATED'

# WF

NOTIFICATION = 'NOTIFICATION'
EMAIL = 'EMAIL'
SMS = 'SMS'

NOT_SEND = 'NOT_SEND'
UNDER_PROCESS = 'UNDER_PROCESS'
FINISHED = 'FINISHED'

# ****

# sheets
SERVICE_AFFAIRS_REGULATION = 'SERVICE_AFFAIRS_REGULATION'
SANCTIONS_REGULATIONS = 'SANCTIONS_REGULATIONS'
ACTIONS_REGULATIONS = 'ACTIONS_REGULATIONS'
NON_DISCLOSURE_AGREEMENT = 'NON_DISCLOSURE_AGREEMENT'
SERVICE_LEVEL_AGREEMENT = 'SERVICE_LEVEL_AGREEMENT'

GLOBAL_SETTINGS = {

    # basic
    SYSTEM_NAME : _('system'),

    ORGANIZATION_CODE: '5040302010', 
    ORGANIZATION_NAME: 'organization name',
    ORGANIZATION_COUNTRY : 'Sudan',

    'WF_NOTIFICATION_CHOICES': {
        NOTIFICATION:  _('notification'),
        EMAIL:  _('email'),
        SMS:  _('sms'),
        },
        
    'YESNO_CHOICES': (
        (YES, _('yes')),
        (NO, _('no')),
    ),

    'STATUS_CHOICES': (
        (WORKING, _('working')),
        (NOTWORKING, _('notworking')),
    ),

    'CONDITION_CHOICES': (
        (NO_MAINTENANCE, _('no maintenance')),
        (MAINTENANCE, _('maintenance')),
        (TO_GET_RIDE, _('to get ride')),
    ),

    'USABILITY_CHOICES': (
        (USED, _('used')),
        (IDLE, _('idle')),
    ),

    'VACANT_VACANCY': (
        (BUSY, _('busy')),
        (NOT_BUSY, _('not busy'))
    ),

    'VACANT_ACTIVATION': (
        (ACTIVATED, _('activated')),
        (NOT_ACTIVATED, _('not activated'))
    ),

    'WF_REQUEST_STATUS': (
        (NOT_SEND, _('not send')),
        (UNDER_PROCESS, _('under process')),
        (FINISHED, _('finished'))
    ),

    'SHEET_LIST': ([
        ('P004',  
            ([
                (SERVICE_AFFAIRS_REGULATION, _('SERVICE_AFFAIRS_REGULATION')),
                (SANCTIONS_REGULATIONS, _('SANCTIONS_REGULATIONS')),
            ])
        ),
        ('P002',  
            ([
                (NON_DISCLOSURE_AGREEMENT, _('NON_DISCLOSURE_AGREEMENT')),
                (SERVICE_LEVEL_AGREEMENT, _('SERVICE_LEVEL_AGREEMENT')),
            ])
        ),
    ]),

}

# CORS_REPLACE_HTTPS_REFERER      = False
# HOST_SCHEME                     = "http://"
# SECURE_PROXY_SSL_HEADER         = None
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE           = False
# CSRF_COOKIE_SECURE              = False
# SECURE_HSTS_SECONDS             = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
# SECURE_FRAME_DENY               = False

# Heroku App

GDAL_LIBRARY_PATH = os.environ.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.environ.get('GEOS_LIBRARY_PATH')

# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# django_heroku.settings(locals())


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
            {'name': 'math', 'items': ['Mathjax', ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        #  'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
         'mathJaxLib': '//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'mathjax',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}