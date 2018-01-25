from .base import *

import os


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['nzimpfer.pythonanywhere.com', ]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'thoufer <thoufer@gmail.com>'

ADMINS = (
    ('nzimpfer', 'thoufer@gmail.com'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'MetadataCatalog',
#         'USER': os.environ['DB_USER'],
#         'PASSWORD': os.environ['DB_PASSWORD'],
#         'HOST': os.environ['DB_HOST'],
#         'PORT': os.envoron['DB_PORT'],
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# pythonanywhere sites by default run on ssl.
#SECURE_HSTS_SECONDS =
#SECURE_SSL_REDIRECT =
