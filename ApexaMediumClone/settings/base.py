from datetime import timedelta
from pathlib import Path
import environ

# Env variable from installed django-environ
env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'
# extra .parent means go 3-levels from this base.py to get to
# root dir where manage.py is located
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Custom Apps directory
APP_DIR = BASE_DIR / "customApps"

# Set debug from env vars, Default is False if not found
DEBUG = env.bool("DJANGO_DEBUG", False)

# Restructured Application definition
DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # added
]

SUPPORT_APPS = [
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "drf_yasg",
    "corsheaders",
    # "djcelery_email",
    # "rest_framework.authtoken",
    # "allauth",
    # "allauth.account",
    # "allauth.socialaccount",
    # "dj_rest_auth",
    # "dj_rest_auth.registration",
    # "taggit",
    # "django_elasticsearch_dsl",
    # "django_elasticsearch_dsl_drf",
]

CUSTOM_APPS = [
    "customApps.common",
    "customApps.profiles",
    "customApps.users",
    # "customApps.articles",
    # "customApps.search",
    # "customApps.ratings",
    # "customApps.bookmarks",
    # "customApps.responses",
]

INSTALLED_APPS = DEFAULT_APPS + SUPPORT_APPS + CUSTOM_APPS

# Default & Custom Middelewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware", # added
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Other Defaults from Django settings
ROOT_URLCONF = "ApexaMediumClone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ApexaMediumClone.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# Set database url from env vars
# will be replaced by docker postgres
DATABASES = {"default": env.db("DATABASE_URL")}

# Custom password hashers from installed argon2
# Built in django password hasher not being used
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# Default Password validators
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "US/Central"

USE_I18N = True

USE_TZ = True

# Set this site id, in case of multiple sites
SITE_ID = 1

# Set Admin url
ADMIN_URL = "super/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR / "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Regex for installed CORS, set url cors headers
# Add cors header to urls starting with api/  
CORS_URLS_REGEX = r"^api/.*$"

# # Set custom User model, not using built in User model
# AUTH_USER_MODEL = "users.User"

# CELERY_BROKER_URL = env("CELERY_BROKER")
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# CELERY_ACCEPT_CONTENT = ["json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_RESULT_BACKEND_MAX_RETRIES = 10
# CELERY_TASK_SEND_SENT_EVENT = True

# if USE_TZ:
#     CELERY_TIMEZONE = TIME_ZONE

# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": [
#         "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
#     ],
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.IsAuthenticated",
#     ],
#     "DEFAULT_FILTER_BACKENDS": [
#         "django_filters.rest_framework.DjangoFilterBackend",
#     ],
# }

# SIMPLE_JWT = {
#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "ROTATE_REFRESH_TOKENS": True,
#     "SIGNING_KEY": env("SIGNING_KEY"),
#     "USER_ID_FIELD": "id",
#     "USER_ID_CLAIM": "user_id",
# }

# REST_AUTH = {
#     "USE_JWT": True,
#     "JWT_AUTH_COOKIE": "authors-access-token",
#     "JWT_AUTH_REFRESH_COOKIE": "authors-refresh-token",
#     "REGISTER_SERIALIZER": "core_apps.users.serializers.CustomRegisterSerializer",
# }

# AUTHENTICATION_BACKENDS = [
#     "allauth.account.auth_backends.AuthenticationBackend",
#     "django.contrib.auth.backends.ModelBackend",
# ]

# ACCOUNT_AUTHENTICATION_METHOD = "email"
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_USERNAME_REQUIRED = False

# ELASTICSEARCH_DSL = {
#     "default": {
#         "hosts": "es:9200",
#     },
# }

# Set Django Logging, for console logs
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(name)-12s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}
