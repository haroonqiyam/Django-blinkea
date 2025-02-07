# Generated by Django 5.1.4 on 2025-01-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='background_color',
            field=models.CharField(blank=True, help_text='Hex code for background color (e.g., #B91C1C)', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='background_image',
            field=models.ImageField(blank=True, help_text='Background image for the banner', null=True, upload_to='banners/backgrounds/'),
        ),
    ]
