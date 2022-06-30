from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birthday = models.DateField(blank=True, null=True)

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'


class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RoleGroup(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f"{self.org.name} group"
