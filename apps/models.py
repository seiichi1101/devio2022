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


class RoleType(models.TextChoices):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'


class Role(models.Model):
    type = models.TextField(
        choices=RoleType.choices, default=RoleType.VIEWER)

    def __str__(self):
        return self.type


def get_default_role():
    role, _ = Role.objects.get_or_create(type=RoleType.VIEWER)
    return role.id


class RoleGroup(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ManyToManyField(CustomUser)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, default=get_default_role)

    def __str__(self):
        return f"{self.org.name} {self.role.type} group"
