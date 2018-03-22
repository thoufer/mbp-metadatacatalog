import os

from .base import *


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]
INTERNAL_IPS = ('127.0.0.1')

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': get_env_variable('DB_ENGINE'),
#         'NAME': get_env_variable('DB_NAME'),
#         'USER': get_env_variable('DB_USER'),
#         'PASSWORD': get_env_variable('DB_PASSWORD'),
#         'HOST': get_env_variable('DB_HOST'),
#         'PORT': get_env_variable('DB_PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
