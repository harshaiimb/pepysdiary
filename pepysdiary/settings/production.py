from defaults import *
from os import environ
import dj_database_url

DEBUG = False

ADMINS = [
    ('Phil Gyford', 'phil@gyford.com'),
]

MANAGERS = ADMINS

DATABASES = {'default': dj_database_url.config(
                                    default=environ.get('DATABASE_URL'))}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# If you *don't* want to prepend www to the URL, remove the setting from
# the environment entirely. Otherwise, set to 'True' (or anything tbh).
PREPEND_WWW = True

# See https://devcenter.heroku.com/articles/memcachier#django
environ['MEMCACHE_SERVERS'] = environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
environ['MEMCACHE_USERNAME'] = environ.get('MEMCACHIER_USERNAME', '')
environ['MEMCACHE_PASSWORD'] = environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
  'default': {
    'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

    # Use binary memcache protocol (needed for authentication)
    'BINARY': True,

    # TIMEOUT is not the connection timeout! It's the default expiration
    # timeout that should be applied to keys! Setting it to `None`
    # disables expiration.
    'TIMEOUT': None,

    'OPTIONS': {
        # Enable faster IO
        'tcp_nodelay': True,

        # Keep connection alive
        'tcp_keepalive': True,

        # Timeout settings
        'connect_timeout': 2000, # ms
        'send_timeout': 750 * 1000, # us
        'receive_timeout': 750 * 1000, # us
        '_poll_timeout': 2000, # ms

        # Better failover
        'ketama': True,
        'remove_failed': 1,
        'retry_timeout': 2,
        'dead_timeout': 30,
    }
  }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}


#############################################################################
# PEPYSDIARY-SPECIFIC SETTINGS.

GOOGLE_ANALYTICS_ID = 'UA-89135-2'

GOOGLE_MAPS_API_KEY = environ.get('GOOGLE_MAPS_API_KEY')

# From https://www.google.com/recaptcha/
RECAPTCHA_PUBLIC_KEY = environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = environ.get('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_USE_SSL = True

# Do we use Akismet/TypePad spam checking?
# True/False. If false, no posted comments are checked.
# If True, AKISMET_API_KEY must also be set.
USE_SPAM_CHECK = environ.get('USE_SPAM_CHECK')

# From http://akismet.com/
AKISMET_API_KEY = environ.get('AKISMET_API_KEY')

# From http://mapbox.com/
MAPBOX_MAP_ID = environ.get('MAPBOX_MAP_ID')
MAPBOX_ACCESS_TOKEN = environ.get('MAPBOX_ACCESS_TOKEN')
