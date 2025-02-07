from .models import NavLink
from main.models import HeaderSettings  # Adjust based on your model location


def nav_links_processor(request):
    """Context processor to provide navigation links in templates."""
    return {
        'nav_links': NavLink.objects.filter(is_active=True)  # Only fetch active links
    }

def header_settings_processor(request):
    """Fetch header settings from the database and make them available globally."""
    header_settings = HeaderSettings.objects.first()  # Retrieve the first record

    return {
        "header_settings": header_settings,  # Make settings available in all templates
    }

def header_context(request):
    """Fetch header settings and navigation links dynamically."""
    return {
        "header_settings": HeaderSettings.objects.first(),
        "nav_links": NavLink.objects.filter(is_active=True),
    }