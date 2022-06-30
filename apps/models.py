from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birthday = models.DateField(blank=True, null=True)

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
