from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.helpers import generate_random_number


class CustomUser(AbstractUser):
    """
    Custom user model
    """

    birthday = models.DateField(verbose_name=_('data urodzenia'), blank=True, null=True)
    random_number = models.IntegerField(verbose_name=_('liczba losowa'), default=generate_random_number, null=True)
