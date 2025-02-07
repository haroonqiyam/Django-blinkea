# Generated by Django 5.1.4 on 2025-01-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_headersetting_button_bg_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_color', models.CharField(default='#000000', help_text='Background color of the header (Hex Code)', max_length=7)),
                ('logo', models.ImageField(blank=True, help_text='Upload your logo image', null=True, upload_to='logos/')),
                ('logo_width', models.PositiveIntegerField(default=150, help_text='Logo width in px')),
                ('logo_height', models.PositiveIntegerField(default=42, help_text='Logo height in px')),
                ('menu_item_text_color', models.CharField(default='#FFFFFF', help_text='Text color of navigation menu (Hex Code)', max_length=7)),
                ('menu_item_hover_color', models.CharField(default='#FF0000', help_text='Hover text color of navigation menu (Hex Code)', max_length=7)),
                ('menu_font_size', models.PositiveIntegerField(default=16, help_text='Font size of the navigation menu items')),
                ('button_text', models.CharField(default='My Account', help_text='Text displayed on the right button', max_length=100)),
                ('button_background_color', models.CharField(default='#FF0000', help_text='Background color of the button', max_length=7)),
                ('button_text_color', models.CharField(default='#FFFFFF', help_text='Text color of the button', max_length=7)),
                ('button_hover_background_color', models.CharField(default='#CC0000', help_text='Button hover background color', max_length=7)),
                ('button_hover_text_color', models.CharField(default='#FFFFFF', help_text='Button hover text color', max_length=7)),
                ('button_link', models.URLField(default='/account/', help_text='URL of the button link')),
            ],
        ),
        migrations.DeleteModel(
            name='HeaderSetting',
        ),
    ]
