# Generated by Django 5.1.4 on 2025-01-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_name_navlink_title_navlink_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_bar_height', models.PositiveIntegerField(default=50, help_text='Height of the top bar in px')),
                ('top_bar_background_color', models.CharField(default='#000000', help_text='Background color of the top bar (Hex Code)', max_length=7)),
                ('top_bar_padding', models.PositiveIntegerField(default=20, help_text='Padding inside the top bar (in px)')),
                ('logo', models.ImageField(blank=True, help_text='Upload your site logo', null=True, upload_to='logos/')),
                ('logo_height', models.PositiveIntegerField(default=50, help_text='Height of the logo (in px)')),
                ('nav_menu_text_color', models.CharField(default='#FFFFFF', help_text='Text color of navigation menu (Hex Code)', max_length=7)),
                ('nav_menu_spacing', models.PositiveIntegerField(default=10, help_text='Spacing between menu items (in px)')),
                ('button_text_color', models.CharField(default='#FFFFFF', help_text='Text color of the right button (Hex Code)', max_length=7)),
                ('button_text', models.CharField(default='My Account', help_text='Text displayed on the right button', max_length=100)),
                ('button_width', models.PositiveIntegerField(default=150, help_text='Width of the right button (in px)')),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(),
        ),
    ]
