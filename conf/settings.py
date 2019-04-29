import os

import environ

env = environ.Env()
root_path = environ.Path(__file__) - 2


# -----------------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------------
ENV = env('ENV', default='prod')
assert ENV in ['dev', 'test', 'prod', 'qa']
DEBUG = env.bool('DEBUG', default=False)
BASE_DIR = root_path()
ROOT_URLCONF = 'conf.urls'
WSGI_APPLICATION = 'conf.wsgi.application'

# -----------------------------------------------------------------------------
# Time & Language
# -----------------------------------------------------------------------------
LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')
TIME_ZONE = env('TIMEZONE', default='UTC')
USE_I18N = env('USE_I18N', default=True)
USE_L10N = env('USE_L10N', default=True)
USE_TZ = env('USE_TZ', default=True)

# -----------------------------------------------------------------------------
# Emails
# -----------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = env(
    'EMAIL_BACKEND',
    default='django.core.mail.backends.smtp.EmailBackend')

# -----------------------------------------------------------------------------
# Security and Users
# -----------------------------------------------------------------------------
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
LOGIN_URL = env('LOGIN_URL', default='/login/')
LOGIN_REDIRECT_URL = env('LOGIN_REDIRECT_URL', default='/')

# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------
DJANGO_DATABASE_URL = env.db('DATABASE_URL')
DATABASES = {'default': DJANGO_DATABASE_URL}

# -----------------------------------------------------------------------------
# Applications configuration
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    # First party
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'webpack_loader',

    # Local
    'apps.misc',
]

if ENV == 'dev':
    INSTALLED_APPS += [
        'django_extensions',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root_path('templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.misc.context_processors.django_settings',
            ],
        },
    },
]

# -----------------------------------------------------------------------------
# Static & Media Files
# -----------------------------------------------------------------------------
STATIC_URL = env('STATIC_URL', default='/static/')
STATIC_ROOT = root_path('static')

MEDIA_URL = env('MEDIA_URL', default='/media/')
MEDIA_ROOT = root_path('media')
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_DIRS = (
    ('bundles', root_path('assets/bundles')),
    ('img', root_path('assets/img')),
)

webpack_stats_filename = 'webpack-bundle.%s.json' % ENV
stats_file = os.path.join(root_path('assets/'), webpack_stats_filename)

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': stats_file,
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

# -----------------------------------------------------------------------------
# Django Debug Toolbar
# -----------------------------------------------------------------------------
USE_DEBUG_TOOLBAR = env.bool('USE_DEBUG_TOOLBAR', default=DEBUG)

if USE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar']
    INTERNAL_IPS = ['127.0.0.1']
    MIDDLEWARE.insert(
        0,
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    )
