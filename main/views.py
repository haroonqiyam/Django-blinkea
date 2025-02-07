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

# Home page view
def home(request):
    # Banner Section
    banner = Banner.objects.filter(is_active=True).first()

    # Hero Section
    hero = HeroSection.objects.filter(is_active=True).first()

    # Scroll Portfolio Section
    config = ScrollPortfolioConfig.objects.first()
    logos = ScrollLogo.objects.all()
    thumbnails = ScrollThumbnail.objects.all()

    # Client Section
    clients = Client.objects.filter(is_active=True).order_by("order")
    client_settings = ClientSettings.objects.first()
    if not client_settings:
        client_settings = ClientSettings.objects.create(
            columns=4,
            container_spacing_top=20,
            container_spacing_bottom=20,
            container_spacing_left=20,
            container_spacing_right=20,
        )

    # Portfolio Section
    portfolios = Portfolio.objects.filter(is_active=True).order_by("order")
    portfolio_settings = PortfolioSettings.objects.first()
    if not portfolio_settings:
        portfolio_settings = PortfolioSettings.objects.create(
            section_title="Work Portfolio",
            columns=3,
            container_spacing_top=20,
            container_spacing_bottom=20,
            container_spacing_left=20,
            container_spacing_right=20,
            item_height=300,
        )

    # CTA Section
    cta_section = CTASection.objects.first()

    # Dynamic Sections
    sections = Section.objects.filter(is_active=True).order_by('order')

    # Navigation
    nav_links = NavLink.objects.filter(is_active=True)
    header_settings = HeaderSettings.objects.first()

    # Footer
    footer_links = FooterLink.objects.all()
    pages = Page.objects.filter(is_active=True)
    
    # Context to pass to the template
    context = {
        'banner': banner,
        'hero': hero,
        'config': config,
        'logos': logos,
        'thumbnails': thumbnails,
        'clients': clients,
        'client_settings': client_settings,
        'portfolios': portfolios,
        'portfolio_settings': portfolio_settings,
        'cta_section': cta_section,
        'sections': sections,
        'nav_links': nav_links,
        'header_settings': header_settings,
        'footer_links': footer_links,
        'pages': pages,
    }

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