"""
Django settings for presutah project.
"""

import os
import arches
import inspect
from django.utils.translation import gettext_lazy as _

try:
    from arches.settings import *
except ImportError:
    pass

APP_NAME = 'presutah'
APP_ROOT = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
STATICFILES_DIRS =  (os.path.join(APP_ROOT, 'media'),) + STATICFILES_DIRS

DATATYPE_LOCATIONS.append('presutah.datatypes')
FUNCTION_LOCATIONS.append('presutah.functions')
SEARCH_COMPONENT_LOCATIONS.append('presutah.search_components')
TEMPLATES[0]['DIRS'].append(os.path.join(APP_ROOT, 'functions', 'templates'))
TEMPLATES[0]['DIRS'].append(os.path.join(APP_ROOT, 'widgets', 'templates'))
TEMPLATES[0]['DIRS'].insert(0, os.path.join(APP_ROOT, 'templates'))

LOCALE_PATHS.append(os.path.join(APP_ROOT, 'locale'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r15^(+id5gn93ttpee)(j-g+at^$9-fa^z02@+k%yj8-#1m-5s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'presutah.urls'

# a prefix to append to all elasticsearch indexes, note: must be lower case
ELASTICSEARCH_PREFIX = 'presutah'

ELASTICSEARCH_CUSTOM_INDEXES = []
# [{
#     'module': 'presutah.search_indexes.sample_index.SampleIndex',
#     'name': 'my_new_custom_index' <-- follow ES index naming rules
# }]

LOAD_DEFAULT_ONTOLOGY = False
LOAD_PACKAGE_ONTOLOGIES = True

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",
        "NAME": "presutah",
        "OPTIONS": {},
        "PASSWORD": "postgis",
        "PORT": "5432",
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIRROR": None,
            "NAME": None
        },
        "TIME_ZONE": None,
        "USER": "postgres"
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'arches',
    'arches.app.models',
    'arches.management',
    'guardian',
    'captcha',
    'revproxy',
    'corsheaders',
    'oauth2_provider',
    'django_celery_results',
    'presutah',
    'compressor',
)

ALLOWED_HOSTS = []

SYSTEM_SETTINGS_LOCAL_PATH = os.path.join(APP_ROOT, 'system_settings', 'System_Settings.json')
WSGI_APPLICATION = 'presutah.wsgi.application'

RESOURCE_IMPORT_LOG = os.path.join(APP_ROOT, 'logs', 'resource_import.log')
DEFAULT_RESOURCE_IMPORT_USER = {'username': 'admin', 'userid': 1}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',  # DEBUG, INFO, WARNING, ERROR
            'class': 'logging.FileHandler',
            'filename': os.path.join(APP_ROOT, 'arches.log'),
            'formatter': 'console'
        },
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'arches': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': True
        }
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT =  os.path.join(APP_ROOT)

# Sets default max upload size to 15MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640

# Unique session cookie ensures that logins are treated separately for each app
SESSION_COOKIE_NAME = 'presutah'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    "user_permission": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "user_permission_cache",
    },
}

# Hide nodes and cards in a report that have no data
HIDE_EMPTY_NODES_IN_REPORT = True

DATE_IMPORT_EXPORT_FORMAT = "%Y-%m-%d" # Custom date format for dates imported from and exported to csv

#Identify the usernames and duration (seconds) for which you want to cache the time wheel
CACHE_BY_USER = {'anonymous': 3600 * 24}
TILE_CACHE_TIMEOUT = 600 #seconds
GRAPH_MODEL_CACHE_TIMEOUT = None

MOBILE_OAUTH_CLIENT_ID = ''  #'9JCibwrWQ4hwuGn5fu2u1oRZSs9V6gK8Vu8hpRC4'
MOBILE_DEFAULT_ONLINE_BASEMAP = {'default': 'mapbox://styles/mapbox/streets-v9'}
MOBILE_IMAGE_SIZE_LIMITS = {
    # These limits are meant to be approximates. Expect to see uploaded sizes range +/- 20%
    # Not to exceed the limit defined in DATA_UPLOAD_MAX_MEMORY_SIZE
    "full": min(1500000, DATA_UPLOAD_MAX_MEMORY_SIZE), # ~1.5 Mb
    "thumb": 400,  # max width/height in pixels, this will maintain the aspect ratio of the original image
}

APP_TITLE = 'Preservation Utah'
COPYRIGHT_TEXT = 'All Rights Reserved.'
COPYRIGHT_YEAR = '2021'

ENABLE_CAPTCHA = False
# RECAPTCHA_PUBLIC_KEY = ''
# RECAPTCHA_PRIVATE_KEY = ''
# RECAPTCHA_USE_SSL = False
NOCAPTCHA = True
# RECAPTCHA_PROXY = 'http://127.0.0.1:8000'
if DEBUG is True:
    SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  #<-- Only need to uncomment this for testing without an actual email server
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'xxxx@xxx.com'
# EMAIL_HOST_PASSWORD = 'xxxxxxx'
# EMAIL_PORT = 587

CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'django-db' # Use 'django-cache' if you want to use your cache as your backend
CELERY_TASK_SERIALIZER = 'json'


CELERY_SEARCH_EXPORT_EXPIRES = 24 * 3600  # seconds
CELERY_SEARCH_EXPORT_CHECK = 3600  # seconds

CELERY_BEAT_SCHEDULE = {
    "delete-expired-search-export": {"task": "arches.app.tasks.delete_file", "schedule": CELERY_SEARCH_EXPORT_CHECK,},
    "notification": {"task": "arches.app.tasks.message", "schedule": CELERY_SEARCH_EXPORT_CHECK, "args": ("Celery Beat is Running",),},
}

# By setting RESTRICT_MEDIA_ACCESS to True, media file requests outside of Arches will checked against nodegroup permissions.
RESTRICT_MEDIA_ACCESS = False

# Arches v6 updates
#For search export columns/properties (shp, csv, json) to match resource card order (at a small performance cost), set the following to True:
EXPORT_DATA_FIELDS_IN_CARD_ORDER = False

#If your geometries are not widely distributed, reducing the following below 5000 meters can improve clustering performance:
CLUSTER_DISTANCE_MAX = 5000 #meters

#To prevent guest users from requesting background search exports with Celery, set the following to True:
RESTRICT_CELERY_EXPORT_FOR_ANONYMOUS_USER = False

#Set the following to True if you want to send Celery tasks to the broker without being able to detect Celery. This might be necessary if the worker pool is regulary fully active, with no idle workers, or if you need to run the Celery task using solo pool (e.g. on Windows). You may need to provide another way of monitoring Celery so you can detect when the background task is not available.
CELERY_CHECK_ONLY_INSPECT_BROKER = False


# see https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#how-django-discovers-language-preference
# to see how LocaleMiddleware tries to determine the user's language preference
# (make sure to check your accept headers as they will override the LANGUAGE_CODE setting!)
# also see get_language_from_request in django.utils.translation.trans_real.py
# to see how the language code is derived in the actual code

####### TO GENERATE .PO FILES DO THE FOLLOWING ########
# run the following commands
# language codes used in the command should be in the form (which is slightly different
# form the form used in the LANGUAGE_CODE and LANGUAGES settings below):
# --local={countrycode}_{REGIONCODE} <-- countrycode is lowercase, regioncode is uppercase, also notice the underscore instead of hyphen
# commands to run (to generate files for "British English, German, and Spanish"):
# django-admin.py makemessages --ignore=env/* --local=de --local=en --local=en_GB --local=es  --extension=htm,py
# django-admin.py compilemessages


# default language of the application
# language code needs to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# list of languages to display in the language switcher,
# if left empty or with a single entry then the switch won't be displayed
# language codes need to be all lower case with the form:
# {langcode}-{regioncode} eg: en, en-gb ....
# a list of language codes can be found here http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = [
#   ('de', _('German')),
  ('en', _('English')),
#   ('en-gb', _('British English')),
#   ('es', _('Spanish')),
]

# override this to permenantly display/hide the language switcher
SHOW_LANGUAGE_SWITCH = len(LANGUAGES) > 1


try:
    from .package_settings import *
except ImportError:
    pass

try:
    from .settings_local import *
except ImportError:
    pass
