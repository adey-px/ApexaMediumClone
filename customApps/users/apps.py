"""
- Utils translation allows app to be translated in diff languages
- Verbose name is part of django model, sets readable name for singular object
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "customApps.users"
    verbose_name = _('Users')