from django.shortcuts import render, get_object_or_404
from .models import Page, HeaderSettings, NavLink, FooterLink, Banner, HeroSection, Client, ClientSettings, Portfolio, PortfolioSettings, CTASection, Section, ScrollPortfolioConfig, ScrollLogo, ScrollThumbnail


# Home page view with all sections

# Solutions Page
def header_context(request):
    header_settings = HeaderSettings.objects.first()
    nav_links = NavLink.objects.all()  # Fetch navigation links from CMS
    
    return {
        "header_settings": header_settings,
        "nav_links": nav_links,
    }

from django.db import connection
from django.db.utils import OperationalError, ProgrammingError

def check_table_exists(table_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            return cursor.fetchone() is not None
    except (OperationalError, ProgrammingError):
        return False

# Home page view
def home(request):
    # Initialize empty context
    context = {}
    
    try:
        # Banner Section
        if check_table_exists('main_banner'):
            context['banner'] = Banner.objects.filter(is_active=True).first()

        # Hero Section
        if check_table_exists('main_herosection'):
            context['hero'] = HeroSection.objects.filter(is_active=True).first()

        # Scroll Portfolio Section
        if check_table_exists('main_scrollportfolioconfig'):
            context['config'] = ScrollPortfolioConfig.objects.first()
        if check_table_exists('main_scrolllogo'):
            context['logos'] = ScrollLogo.objects.all()
        if check_table_exists('main_scrollthumbnail'):
            context['thumbnails'] = ScrollThumbnail.objects.all()

        # Client Section
        if check_table_exists('main_client'):
            context['clients'] = Client.objects.filter(is_active=True).order_by("order")
        if check_table_exists('main_clientsettings'):
            client_settings = ClientSettings.objects.first()
            if not client_settings and check_table_exists('main_clientsettings'):
                client_settings = ClientSettings.objects.create(
                    columns=4,
                    container_spacing_top=20,
                    container_spacing_bottom=20,
                    container_spacing_left=20,
                    container_spacing_right=20,
                )
            context['client_settings'] = client_settings

        # Portfolio Section
        if check_table_exists('main_portfolio'):
            context['portfolios'] = Portfolio.objects.filter(is_active=True).order_by("order")
        if check_table_exists('main_portfoliosettings'):
            portfolio_settings = PortfolioSettings.objects.first()
            if not portfolio_settings and check_table_exists('main_portfoliosettings'):
                portfolio_settings = PortfolioSettings.objects.create(
                    section_title="Work Portfolio",
                    columns=3,
                    container_spacing_top=20,
                    container_spacing_bottom=20,
                    container_spacing_left=20,
                    container_spacing_right=20,
                    item_height=300,
                )
            context['portfolio_settings'] = portfolio_settings

        # CTA Section
        if check_table_exists('main_ctasection'):
            context['cta_section'] = CTASection.objects.first()

        # Dynamic Sections
        if check_table_exists('main_section'):
            context['sections'] = Section.objects.filter(is_active=True).order_by('order')

        # Navigation
        if check_table_exists('main_navlink'):
            context['nav_links'] = NavLink.objects.filter(is_active=True)
        if check_table_exists('main_headersettings'):
            context['header_settings'] = HeaderSettings.objects.first()

        # Footer
        if check_table_exists('main_footerlink'):
            context['footer_links'] = FooterLink.objects.all()
        if check_table_exists('main_page'):
            context['pages'] = Page.objects.filter(is_active=True)

    except Exception as e:
        print(f"Error in home view: {str(e)}")
        # Continue with empty or partial context

    return render(request, 'main/home.html', context)



# Page detail view
def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    header_settings = HeaderSettings.objects.first()  # Assuming only one entry for header settings

    # Fetch active pages for the navigation menu
    pages = Page.objects.filter(is_active=True)

    return render(request, 'main/page_details.html', {
        'page': page,
        'pages': pages,  # Pass pages for navigation
        'header_settings': header_settings,  # Pass header settings for dynamic styling
    })


# About page view
def about(request):
    nav_links = NavLink.objects.all()
    footer_links = FooterLink.objects.all()
    return render(request, 'main/about.html', {
        'nav_links': nav_links,
        'footer_links': footer_links,
    })


# Contact page view
def contact(request):
    nav_links = NavLink.objects.all()
    footer_links = FooterLink.objects.all()
    return render(request, 'main/contact.html', {
        'nav_links': nav_links,
        'footer_links': footer_links,
    })