# Generated by Django 5.1.4 on 2025-01-01 17:11

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_headersetting_alter_page_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headersetting',
            name='logo',
            field=models.ImageField(blank=True, help_text='Upload your site logo', null=True, storage=django.core.files.storage.FileSystemStorage(location='BlinkeaProject/main/static/images/'), upload_to='logos/'),
        ),
    ]
