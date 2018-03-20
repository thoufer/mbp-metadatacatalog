import os

from .base import *


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['www.migbirddatacatalog.us',]

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# DEFAULT_FROM_EMAIL = 'thoufer <thoufer@gmail.com>'

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': get_env_variable('DB_ENGINE'),
        'OPTIONS': {
            'sql_mode': 'STRICT_ALL_TABLES'
            },
        'NAME': get_env_variable('DB_USER') + '$' + get_env_variable('DB_NAME'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'HOST': get_env_variable('DB_HOST'),
        'PORT': get_env_variable('DB_PORT'),
     }
}

# disable browsable api in production
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# pythonanywhere sites by default run on ssl.
SECURE_HSTS_SECONDS = 3600
SECURE_SSL_REDIRECT = True
