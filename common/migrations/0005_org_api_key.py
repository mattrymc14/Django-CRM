# Generated by Django 4.2.1 on 2023-11-02 11:19

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_profile_alternate_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='org',
            name='api_key',
            field=models.TextField(default=common.models.generate_unique_key, editable=False),
        ),
    ]