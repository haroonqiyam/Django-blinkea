# Generated by Django 5.1.4 on 2025-01-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_headersettings_logo_width_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='headersettings',
            name='button_bottom_padding',
            field=models.PositiveIntegerField(default=10, help_text='Bottom padding for the button in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='button_left_padding',
            field=models.PositiveIntegerField(default=10, help_text='Left padding for the button in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='button_right_padding',
            field=models.PositiveIntegerField(default=10, help_text='Right padding for the button in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='button_top_padding',
            field=models.PositiveIntegerField(default=10, help_text='Top padding for the button in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='container_bottom_padding',
            field=models.PositiveIntegerField(default=10, help_text='Bottom padding for the header container (black box) in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='container_left_padding',
            field=models.PositiveIntegerField(default=10, help_text='Left padding for the header container (black box) in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='container_right_padding',
            field=models.PositiveIntegerField(default=10, help_text='Right padding for the header container (black box) in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='container_top_padding',
            field=models.PositiveIntegerField(default=10, help_text='Top padding for the header container (black box) in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_bottom_padding',
            field=models.PositiveIntegerField(default=10, help_text='Bottom padding for the logo in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_left_padding',
            field=models.PositiveIntegerField(default=10, help_text='Left padding for the logo in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_right_padding',
            field=models.PositiveIntegerField(default=10, help_text='Right padding for the logo in px'),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='logo_top_padding',
            field=models.PositiveIntegerField(default=10, help_text='Top padding for the logo in px'),
        ),
    ]
