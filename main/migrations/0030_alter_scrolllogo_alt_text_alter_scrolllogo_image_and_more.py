# Generated by Django 5.1.4 on 2025-01-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_scrolllogo_scrollportfolioconfig_scrollthumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrolllogo',
            name='alt_text',
            field=models.CharField(blank=True, help_text='Alternative text for the logo for accessibility.', max_length=100),
        ),
        migrations.AlterField(
            model_name='scrolllogo',
            name='image',
            field=models.ImageField(help_text='Upload the logo image.', upload_to='logos/'),
        ),
        migrations.AlterField(
            model_name='scrollportfolioconfig',
            name='logo_scroll_speed',
            field=models.FloatField(default=10, help_text='Speed of the logo scrolling (in seconds). Lower values mean faster scrolling.'),
        ),
        migrations.AlterField(
            model_name='scrollportfolioconfig',
            name='logo_width',
            field=models.PositiveIntegerField(default=100, help_text='Width of each logo in pixels. Set the desired width; height adjusts proportionally.'),
        ),
        migrations.AlterField(
            model_name='scrollportfolioconfig',
            name='thumbnail_scroll_speed',
            field=models.FloatField(default=10, help_text='Speed of the thumbnail scrolling (in seconds). Lower values mean faster scrolling.'),
        ),
        migrations.AlterField(
            model_name='scrollportfolioconfig',
            name='thumbnail_width',
            field=models.PositiveIntegerField(default=150, help_text='Width of each thumbnail in pixels. Set the desired width; height adjusts proportionally.'),
        ),
        migrations.AlterField(
            model_name='scrollthumbnail',
            name='alt_text',
            field=models.CharField(blank=True, help_text='Alternative text for the thumbnail for accessibility.', max_length=100),
        ),
        migrations.AlterField(
            model_name='scrollthumbnail',
            name='image',
            field=models.ImageField(help_text='Upload the thumbnail image.', upload_to='thumbnails/'),
        ),
        migrations.AlterField(
            model_name='scrollthumbnail',
            name='link',
            field=models.URLField(help_text='URL to navigate when the thumbnail is clicked.'),
        ),
        migrations.AlterField(
            model_name='section',
            name='template_name',
            field=models.CharField(choices=[('main/banner.html', 'Banner'), ('main/scrollportfolio.html', 'Scroll Panel'), ('main/hero.html', 'Hero'), ('main/clients.html', 'Clients & Partners'), ('main/portfolio.html', 'Portfolio'), ('main/cta.html', 'Call to Action')], help_text='Choose the template for this section', max_length=100),
        ),
    ]
