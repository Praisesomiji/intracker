# Generated by Django 4.2.14 on 2024-08-10 07:26

import django.core.validators
from django.db import migrations, models
import planner.models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf']), planner.models.validate_file_size]),
        ),
    ]
