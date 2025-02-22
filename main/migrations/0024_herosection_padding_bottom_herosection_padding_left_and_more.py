# Generated by Django 5.1.4 on 2025-01-03 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_ctasection'),
    ]

    operations = [
        migrations.AddField(
            model_name='herosection',
            name='padding_bottom',
            field=models.PositiveIntegerField(default=64, help_text='Bottom padding for the container in pixels'),
        ),
        migrations.AddField(
            model_name='herosection',
            name='padding_left',
            field=models.PositiveIntegerField(default=16, help_text='Left padding for the container in pixels'),
        ),
        migrations.AddField(
            model_name='herosection',
            name='padding_right',
            field=models.PositiveIntegerField(default=16, help_text='Right padding for the container in pixels'),
        ),
        migrations.AddField(
            model_name='herosection',
            name='padding_top',
            field=models.PositiveIntegerField(default=64, help_text='Top padding for the container in pixels'),
        ),
    ]
