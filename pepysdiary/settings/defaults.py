# Django settings for pepysdiary project.

# Should be extended by settings in, eg, production.py.
import os
from os import environ

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DEBUG = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_collected/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'common', 'static'),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

MIDDLEWARE = [
    # Must be first:
    'django.middleware.cache.UpdateCacheMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pepysdiary.common.middleware.VisitTimeMiddleware',
    # Must be last:
    'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHE_MIDDLEWARE_ALIAS = 'default'
# Also see the CACHES setting in the server-specific settings files.
CACHE_MIDDLEWARE_SECONDS = 500
CACHE_MIDDLEWARE_KEY_PREFIX = 'pepys'

ROOT_URLCONF = 'pepysdiary.common.urls'

# Make this unique, and don't share it with anybody.
# http://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = environ.get('SECRET_KEY', '')

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '*').split(',')

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pepysdiary.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'treebeard/templates/',
            os.path.join(PROJECT_ROOT, 'templates', ),
            os.path.join(PROJECT_ROOT, 'templates', 'common', ),
            os.path.join(PROJECT_ROOT, 'templates', 'diary', ),
            os.path.join(PROJECT_ROOT, 'templates', 'encyclopedia', ),
            os.path.join(PROJECT_ROOT, 'templates', 'letters', ),
            os.path.join(PROJECT_ROOT, 'templates', 'news', ),
            os.path.join(PROJECT_ROOT, 'templates', 'membership', ),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',

                # Needed for django-treebeard admin:
                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'pepysdiary.common.context_processors.api_keys',
                'pepysdiary.common.context_processors.config',
                'pepysdiary.common.context_processors.date_formats',
                'pepysdiary.common.context_processors.url_name',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Use Whitenoise instead of Django's static file handling in development:
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.flatpages',
    'treebeard',
    'gunicorn',
    'captcha',

    # Started breaking with Django 1.10.7 although it shouldn't:
    # 'memcache_status',

    'pepysdiary.common',
    'pepysdiary.diary',
    'pepysdiary.encyclopedia',
    'pepysdiary.letters',
    'pepysdiary.indepth',
    'pepysdiary.news',
    'pepysdiary.membership',
    'pepysdiary.events',
    'django_comments',
    'pepysdiary.annotations',
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'membership.Person'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

COMMENTS_APP = 'pepysdiary.annotations'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'



####################################################################
# THIRD-PARTY APPS

from datetime import date, timedelta
future_date = date.today() + timedelta(days=365)

# From https://github.com/praekelt/django-recaptcha
NOCAPTCHA = True

# Storing Media files on AWS.

DEFAULT_FILE_STORAGE = 'pepysdiary.common.s3utils.MediaS3Boto3Storage'

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_QUERYSTRING_AUTH = False

S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# Store static and media files in separate directories:
MEDIA_URL = S3_URL + MEDIA_URL


####################################################################
# PEPYSDIARY SPECIFIC

# For messages we send to users.
DEFAULT_FROM_EMAIL = 'do-not-reply@pepysdiary.com'
# For error messages.
SERVER_EMAIL = 'do-not-reply@pepysdiary.com'

# How many days do we give people to activate their account after registering?
# If we run the cleanupactivation command, it will delete any dormant
# activations older than this:
ACCOUNT_ACTIVATION_DAYS = 7

# How many years ahead of the diary entries are we?
YEARS_OFFSET = 353

# We have to do special things to some Encyclopedia Topics depending on
# whether they're in the 'People' category. So we need to store its ID:
PEOPLE_CATEGORY_ID = 2

# We have a Topic for Samuel Pepys, which occasionally needs special
# treatment, so we store its ID here:
PEPYS_TOPIC_ID = 29


# The IDs of the various Movable Type blogs that we do one-off imports of data
# from:
MT_DIARY_BLOG_ID = 3
MT_ENCYCLOPEDIA_BLOG_ID = 4
MT_IN_DEPTH_BLOG_ID = 19
MT_NEWS_BLOG_ID = 5
MT_STORY_SO_FAR_BLOG_ID = 6
MT_LETTERS_BLOG_ID = 38
