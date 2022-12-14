# Generated by Django 3.2.1 on 2022-06-30 11:53

import apps.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_organization_rolegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(choices=[('admin', 'Admin'), ('editor', 'Editor'), ('viewer', 'Viewer')], default='viewer')),
            ],
        ),
        migrations.AddField(
            model_name='rolegroup',
            name='role',
            field=models.ForeignKey(default=apps.models.get_default_role, on_delete=django.db.models.deletion.CASCADE, to='apps.role'),
        ),
    ]
