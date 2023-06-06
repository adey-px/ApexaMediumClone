from .base import * #noqa - tells linter to ignore this line
from .base import env

# Get secret key from env vars, use default if not found
# Default generated from Python secret module
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="3vcDgmaLCk42kTKG_Y46uvH9rX7FWIP0fO3ctzf_VrGaRCBvNAQ",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Set trusted origins, domains allowed for cross-site request
# Here is Ngnix server domain for reverse proxy
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

# 
# EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
# EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
# EMAIL_PORT = env("EMAIL_PORT")
# DEFAULT_FROM_EMAIL = "support@apiimperfect.site"

# # 
# DOMAIN = env("DOMAIN")
# SITE_NAME = "Authors Haven"
