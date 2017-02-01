# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import environ
import os

ROOT_DIR = environ.Path(__file__) - 4  # 'alchemy-ui directory, which is this project's root'

SERVER_DIR = ROOT_DIR.path('src')
SERVER_PATH = str(SERVER_DIR.path())

CLIENT_DIR = ROOT_DIR.path('client')
CLIENT_PATH = str(CLIENT_DIR.path())

env = environ.Env()
environ.Env.read_env('.env')

# ------------------------------------------------------------------------------
# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# ------------------------------------------------------------------------------
# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    'flat',
    'overextends',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
    'rest_framework.authtoken',
)

LOCAL_APPS = (
    'apps.api',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------------------------------------------------------------------------
# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------------------------------
# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)

# ------------------------------------------------------------------------------
# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DJANGO_DB_NAME'),
        'USER': env('DJANGO_DB_USER'),
        'PASSWORD': env('DJANGO_DB_PASSWORD'),
        'HOST': env('DJANGO_DB_HOST'),
        'PORT': env('DJANGO_DB_PORT'),
    },
}

# ------------------------------------------------------------------------------
# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = env.bool("DJANGO_ALLOWED_HOSTS", default=['*', ])

# ------------------------------------------------------------------------------
# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(SERVER_PATH, 'templates'),
    ],
    'OPTIONS': {
        'debug': DEBUG,
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.i18n',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
        ],
    },
}]

if not DEBUG:
    TEMPLATES[0]['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]


# ------------------------------------------------------------------------------
# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(SERVER_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = env("STATIC_ROOT", default="assets")

# ------------------------------------------------------------------------------
# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

MEDIA_ROOT = str(SERVER_DIR('media'))
MEDIA_URL = '/media/'

ROOT_URLCONF = 'config.urls'

# ------------------------------------------------------------------------------
# OTHER Configuration
# ------------------------------------------------------------------------------
ADMINS = (
    ("""admin""", ''),
)
MANAGERS = ADMINS

# ------------------------------------------------------------------------------
# LOGGIN INFORMATION
# ------------------------------------------------------------------------------
LOG_DIR = env("LOG_DIR", default=str(ROOT_DIR) + '/logs/')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(levelname)s] -- %(asctime)s -- %(module)s:%(lineno)s ___ %(message)s >>> "
                      "{ process: %(process)d | thread: %(thread)d }",
            'datefmt': "%b %e, %I:%M:%S %p"
        },
        'simple': {
            'format': '[%(levelname)s] -- %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', ],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_DIR + 'django.log',
            'maxBytes': 20 * 1024 * 1024,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'apps': {
            'handlers': ['log_file', 'console', ],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['log_file', 'mail_admins', ],
            'level': 'INFO',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'INFO',
            'handlers': ['log_file', 'console', 'mail_admins', ],
            'propagate': True
        },
    },
}


# ------------------------------------------------------------------------------
# DJANGO REST FRAMEWORK SETTINGS
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'ALLOWED_VERSIONS': ('v1.0',),
    'DEFAULT_VERSION': 'v1.0',
}
