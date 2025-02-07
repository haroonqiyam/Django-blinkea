# Generated by Django 5.1.4 on 2025-01-03 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_section_options_remove_section_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='template_name',
            field=models.CharField(choices=[('main/banner.html', 'Banner'), ('main/hero.html', 'Hero'), ('main/clients.html', 'Clients & Partners'), ('main/portfolio.html', 'Portfolio'), ('main/cta.html', 'Call to Action')], help_text='Choose the template for this section', max_length=100),
        ),
    ]
