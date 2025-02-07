from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.translation import gettext_lazy as _


# Scrolling Portfolio and scroll logo
class ScrollPortfolioConfig(models.Model):
    """
    Configuration for the scrolling portfolio section, including background color,
    logo panel settings, and thumbnail panel settings.
    """
    # Background Configuration
    background_color = models.CharField(
        max_length=50,
        default="linear-gradient(to right, navy, purple)",
        help_text="CSS background property value (e.g., 'linear-gradient(to right, navy, purple)' or '#ffffff')"
    )

    # Logo Panel Settings
    logo_scroll_speed = models.FloatField(
        default=10,
        help_text="Speed of the logo scrolling (in seconds). Lower values mean faster scrolling."
    )
    logo_width = models.PositiveIntegerField(
        default=100,
        help_text="Width of each logo in pixels. Set the desired width; height adjusts proportionally."
    )

    # Thumbnail Panel Settings
    thumbnail_scroll_speed = models.FloatField(
        default=10,
        help_text="Speed of the thumbnail scrolling (in seconds). Lower values mean faster scrolling."
    )
    thumbnail_width = models.PositiveIntegerField(
        default=380,
        help_text="Width of each thumbnail in pixels. Set the desired width; height adjusts proportionally."
    )

    def __str__(self):
        return "Scroll Portfolio Configuration"


class ScrollLogo(models.Model):
    """
    Represents a logo in the scrolling portfolio. Logos are displayed with a dynamic width
    based on the ScrollPortfolioConfig settings.
    """
    image = models.ImageField(
        upload_to="logos/",
        help_text="Upload the logo image."
    )
    alt_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Alternative text for the logo for accessibility."
    )

    def __str__(self):
        return self.alt_text or f"Logo {self.id}"


class ScrollThumbnail(models.Model):
    """
    Represents a thumbnail in the scrolling portfolio. Thumbnails are clickable and link
    to external or internal URLs.
    """
    image = models.ImageField(
        upload_to="thumbnails/",
        help_text="Upload the thumbnail image."
    )
    link = models.URLField(
        help_text="URL to navigate when the thumbnail is clicked."
    )
    alt_text = models.CharField(
        max_length=100,
        blank=True,
        help_text="Alternative text for the thumbnail for accessibility."
    )

    def __str__(self):
        return self.alt_text or f"Thumbnail {self.id}"


# Re Arrange home order
class Section(models.Model):
    TEMPLATE_CHOICES = [
        ('main/banner.html', 'Banner'),
        ('main/scrollportfolio.html', 'Scroll Panel'),
        ('main/hero.html', 'Hero'),
        ('main/clients.html', 'Clients & Partners'),
        ('main/portfolio.html', 'Portfolio'),
        ('main/cta.html', 'Call to Action'),
    ]

    name = models.CharField(max_length=100)
    template_name = models.CharField(
        max_length=100,
        choices=TEMPLATE_CHOICES,
        help_text="Choose the template for this section"
    )
    order = models.PositiveIntegerField(default=0, help_text="Order of the section")
    is_active = models.BooleanField(default=True, help_text="Show this section on the homepage")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


# CTA section
class CTASection(models.Model):
    title = models.CharField(max_length=255, help_text="CTA Title Text")
    title_color = models.CharField(max_length=7, default="#FFFFFF", help_text="Title text color (HEX code)")
    title_size = models.IntegerField(default=24, help_text="Title font size in pixels")
    title_alignment = models.CharField(
        max_length=10,
        choices=[("left", "Left"), ("center", "Center"), ("right", "Right")],
        default="left",
        help_text="Title text alignment"
    )
    container_height = models.CharField(max_length=50, default="auto", help_text="Height of the container (e.g., auto, 400px)")
    bg_color_start = models.CharField(max_length=7, default="#1E3A8A", help_text="Background gradient start color (HEX)")
    bg_color_end = models.CharField(max_length=7, default="#1D4ED8", help_text="Background gradient end color (HEX)")
    padding_top = models.IntegerField(default=64, help_text="Top padding in pixels")
    padding_bottom = models.IntegerField(default=64, help_text="Bottom padding in pixels")
    padding_left = models.IntegerField(default=16, help_text="Left padding in pixels")
    padding_right = models.IntegerField(default=16, help_text="Right padding in pixels")
    button_text = models.CharField(max_length=50, default="Get a quote now →", help_text="Button text")
    button_text_color = models.CharField(max_length=7, default="#FFFFFF", help_text="Button text color (HEX code)")
    button_color = models.CharField(max_length=7, default="#EF4444", help_text="Button background color (HEX code)")
    button_width = models.CharField(max_length=50, default="auto", help_text="Button width (e.g., auto, 200px)")
    button_url = models.URLField(default="#", help_text="URL for the CTA button")  # Add the URL field

    def __str__(self):
        return f"CTA Section - {self.title[:30]}"

    class Meta:
        verbose_name = "CTA Section"
        verbose_name_plural = "CTA Sections"


# <------- START OF Portfolio Model ------->
class Portfolio(models.Model):
    # Portfolio Item Title
    title = models.CharField(
        max_length=255,
        help_text="Title of the portfolio item",
    )

    # Thumbnail Image
    thumbnail_image = models.ImageField(
        upload_to="portfolio/thumbnails/",
        help_text="Thumbnail image for the portfolio item",
    )

    # Hover Image
    hover_image = models.ImageField(
        upload_to="portfolio/hover/",
        blank=True,
        null=True,
        help_text="Image to display on mouse hover",
    )
    
    # Description
    description = models.TextField(
        help_text="Short description of the portfolio item",
    )

    # Detail Page URL
    detail_url = models.URLField(
        help_text="Link to the detailed portfolio page",
    )

    # Display Order
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which the portfolio item appears",
    )

    # Active Status
    is_active = models.BooleanField(
        default=True,
        help_text="Show this portfolio item on the site",
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# portfolio setting
class PortfolioSettings(models.Model):
    # Section Title
    section_title = models.CharField(
        max_length=255,
        default="Work Portfolio",
        help_text="Title for the portfolio section",
    )

    # Grid Columns
    columns = models.PositiveIntegerField(
        default=3,
        help_text="Number of portfolio items per row",
    )

    # Background Color
    container_background_color = models.CharField(
        max_length=7,
        default="#FFFFFF",
        help_text="Background color of the portfolio container (Hex Code, e.g., #FFFFFF for white)",
    )

    # Container Padding
    container_spacing_top = models.PositiveIntegerField(
        default=20,
        help_text="Top padding for the portfolio container (in px)",
    )
    container_spacing_bottom = models.PositiveIntegerField(
        default=20,
        help_text="Bottom padding for the portfolio container (in px)",
    )
    container_spacing_left = models.PositiveIntegerField(
        default=20,
        help_text="Left padding for the portfolio container (in px)",
    )
    container_spacing_right = models.PositiveIntegerField(
        default=20,
        help_text="Right padding for the portfolio container (in px)",
    )

    # Item Height
    item_height = models.PositiveIntegerField(
        default=300,
        help_text="Height of each portfolio item in px",
    )

    def __str__(self):
        return "Portfolio Settings"
    
    # <----- END OF PORTFOLIO MODEL ----->



# Client list model

class Client(models.Model):
    # Client Name
    name = models.CharField(
        max_length=255,
        help_text="Name of the client or partner",
    )

    # Client Logo
    logo = models.ImageField(
        upload_to="clients/logos/",
        blank=True,
        null=True,
        help_text="Upload the client's logo",
    )

    # Display Order
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which the client appears in the list",
    )

    # Active Status
    is_active = models.BooleanField(
        default=True,
        help_text="Show this client in the clients section",
    )

    class Meta:
        ordering = ["order"]  # Display clients based on their order

    def __str__(self):
        return self.name


class ClientSettings(models.Model):
    # Number of columns in the grid
    columns = models.PositiveIntegerField(
        default=4,
        help_text="Number of clients to display per row.",
    )

    # Spacing settings
    container_spacing_top = models.PositiveIntegerField(
        default=20,
        help_text="Top spacing for the container (in pixels)."
    )
    container_spacing_bottom = models.PositiveIntegerField(
        default=20,
        help_text="Bottom spacing for the container (in pixels)."
    )
    container_spacing_left = models.PositiveIntegerField(
        default=20,
        help_text="Left spacing for the container (in pixels)."
    )
    container_spacing_right = models.PositiveIntegerField(
        default=20,
        help_text="Right spacing for the container (in pixels)."
    )

    def __str__(self):
        return "Client Section Settings"
    
# <------ Client End here -------->

# Hero Section with gradient background
class HeroSection(models.Model):
    # General Settings
    background_color_from = models.CharField(
        max_length=50, 
        default="#991B1B", 
        help_text="Gradient start color (e.g., #991B1B for red-800)"
    )
    background_color_to = models.CharField(
        max_length=50, 
        default="#1E3A8A", 
        help_text="Gradient end color (e.g., #1E3A8A for blue-900)"
    )
    text_color = models.CharField(
        max_length=50, 
        default="#FFFFFF", 
        help_text="Text color (e.g., #FFFFFF for white)"
    )

    # Container Spacing
    padding_top = models.PositiveIntegerField(default=64, help_text="Top padding for the container in pixels")
    padding_bottom = models.PositiveIntegerField(default=64, help_text="Bottom padding for the container in pixels")
    padding_left = models.PositiveIntegerField(default=16, help_text="Left padding for the container in pixels")
    padding_right = models.PositiveIntegerField(default=16, help_text="Right padding for the container in pixels")

    # Main Heading
    main_heading = models.CharField(max_length=255, help_text="Main heading text")
    main_heading_size = models.PositiveIntegerField(default=48, help_text="Font size for main heading in pixels")
    main_heading_spacing_top = models.PositiveIntegerField(default=0, help_text="Top margin for the main heading")
    main_heading_spacing_bottom = models.PositiveIntegerField(default=16, help_text="Bottom margin for the main heading")

    # Subheading
    subheading = models.TextField(help_text="Subheading text")
    subheading_size = models.PositiveIntegerField(default=18, help_text="Font size for subheading in pixels")
    subheading_spacing_top = models.PositiveIntegerField(default=16, help_text="Top margin for the subheading")
    subheading_spacing_bottom = models.PositiveIntegerField(default=24, help_text="Bottom margin for the subheading")

    # Buttons
    button_1_text = models.CharField(max_length=100, help_text="Text for the first button")
    button_1_url = models.URLField(help_text="URL for the first button")
    button_1_bg_color = models.CharField(max_length=50, default="#DC2626", help_text="Background color for the first button")
    button_1_text_color = models.CharField(max_length=50, default="#FFFFFF", help_text="Text color for the first button")

    button_2_text = models.CharField(max_length=100, help_text="Text for the second button")
    button_2_url = models.URLField(help_text="URL for the second button")
    button_2_border_color = models.CharField(max_length=50, default="#FFFFFF", help_text="Border color for the second button")
    button_2_text_color = models.CharField(max_length=50, default="#FFFFFF", help_text="Text color for the second button")
    button_2_hover_bg_color = models.CharField(max_length=50, default="#FFFFFF", help_text="Hover background color for the second button")
    button_2_hover_text_color = models.CharField(max_length=50, default="#000000", help_text="Hover text color for the second button")

    # Clients Info
    clients_info = models.TextField(help_text="Text for clients info")
    clients_info_color = models.CharField(max_length=50, default="#D1D5DB", help_text="Text color for clients info")
    clients_info_spacing_top = models.PositiveIntegerField(default=32, help_text="Top margin for clients info")

    is_active = models.BooleanField(default=True, help_text="Display this hero section on the site")

    def __str__(self):
        return "Hero Section"
    

# Top Menu pages
class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    

# Header model for navigation links
class NavLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)  # This could also be a ForeignKey to a Page model
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Footer model for social links
class FooterLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name
    

# Header Setting
class HeaderSettings(models.Model):
    # Background Color
    background_color = models.CharField(max_length=7, default='#000000', help_text="Background color of the header (Hex Code)")
    
    # Logo
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload your logo image")
    logo_height = models.PositiveIntegerField(default=42, help_text="Logo height in px")
    
    # Logo Padding (top, bottom, left, right)
    logo_top_padding = models.PositiveIntegerField(default=10, help_text="Top padding for the logo in px")
    logo_bottom_padding = models.PositiveIntegerField(default=10, help_text="Bottom padding for the logo in px")
    logo_left_padding = models.PositiveIntegerField(default=10, help_text="Left padding for the logo in px")
    logo_right_padding = models.PositiveIntegerField(default=10, help_text="Right padding for the logo in px")

    # Menu Links
    menu_item_text_color = models.CharField(max_length=7, default='#FFFFFF', help_text="Text color of navigation menu (Hex Code)")
    menu_item_hover_color = models.CharField(max_length=7, default='#FF0000', help_text="Hover text color of navigation menu (Hex Code)")
    menu_font_size = models.PositiveIntegerField(default=16, help_text="Font size of the navigation menu items")

    # Button Settings
    button_text = models.CharField(max_length=100, default='My Account', help_text="Text displayed on the right button")
    button_background_color = models.CharField(max_length=7, default='#FF0000', help_text="Background color of the button")
    button_text_color = models.CharField(max_length=7, default='#FFFFFF', help_text="Text color of the button")
    button_hover_background_color = models.CharField(max_length=7, default='#CC0000', help_text="Button hover background color")
    button_hover_text_color = models.CharField(max_length=7, default='#FFFFFF', help_text="Button hover text color")
    button_link = models.URLField(default='/account/', help_text="URL of the button link")

    # Button Padding (top, bottom, left, right)
    button_top_padding = models.PositiveIntegerField(default=10, help_text="Top padding for the button in px")
    button_bottom_padding = models.PositiveIntegerField(default=10, help_text="Bottom padding for the button in px")
    button_left_padding = models.PositiveIntegerField(default=10, help_text="Left padding for the button in px")
    button_right_padding = models.PositiveIntegerField(default=10, help_text="Right padding for the button in px")

    # Header Height
    header_height = models.PositiveIntegerField(default=120, help_text="Height of the header in px")

    # Header Container Padding (top, bottom, left, right)
    container_top_padding = models.PositiveIntegerField(default=10, help_text="Top padding for the header container (black box) in px")
    container_bottom_padding = models.PositiveIntegerField(default=10, help_text="Bottom padding for the header container (black box) in px")
    container_left_padding = models.PositiveIntegerField(default=10, help_text="Left padding for the header container (black box) in px")
    container_right_padding = models.PositiveIntegerField(default=10, help_text="Right padding for the header container (black box) in px")

    def reset_to_default(self):
        """ Reset all fields to default values """
        self.background_color = '#000000'
        self.menu_item_text_color = '#FFFFFF'
        self.menu_item_hover_color = '#FF0000'
        self.menu_font_size = 16
        self.button_text = 'My Account'
        self.button_background_color = '#FF0000'
        self.button_text_color = '#FFFFFF'
        self.button_hover_background_color = '#CC0000'
        self.button_hover_text_color = '#FFFFFF'
        self.button_link = '/account/'
        self.header_height = 120  # Reset to default height
        self.container_top_padding = 10
        self.container_bottom_padding = 10
        self.container_left_padding = 10
        self.container_right_padding = 10
        self.logo_top_padding = 10
        self.logo_bottom_padding = 10
        self.logo_left_padding = 10
        self.logo_right_padding = 10
        self.button_top_padding = 10
        self.button_bottom_padding = 10
        self.button_left_padding = 10
        self.button_right_padding = 10
        self.save()

    def __str__(self):
        return "Header Settings"
    

# Red Banner
class Banner(models.Model):
    title = models.CharField(max_length=255, help_text="Title displayed on the banner")
    title_spacing_top = models.PositiveIntegerField(default=0, help_text="Top spacing for the title (in pixels)")
    title_spacing_bottom = models.PositiveIntegerField(default=16, help_text="Bottom spacing for the title (in pixels)")

    subtitle = models.CharField(max_length=255, help_text="Subtitle displayed on the banner")
    subtitle_spacing_top = models.PositiveIntegerField(default=16, help_text="Top spacing for the subtitle (in pixels)")
    subtitle_spacing_bottom = models.PositiveIntegerField(default=16, help_text="Bottom spacing for the subtitle (in pixels)")

    image = models.ImageField(upload_to='banners/', help_text="Image for the banner")
    image_spacing_top = models.PositiveIntegerField(default=16, help_text="Top spacing for the image (in pixels)")
    image_spacing_bottom = models.PositiveIntegerField(default=16, help_text="Bottom spacing for the image (in pixels)")

    button_text = models.CharField(max_length=100, help_text="Text for the call-to-action button")
    button_link = models.URLField(help_text="Link for the call-to-action button")
    button_spacing_top = models.PositiveIntegerField(default=16, help_text="Top spacing for the button (in pixels)")
    button_spacing_bottom = models.PositiveIntegerField(default=0, help_text="Bottom spacing for the button (in pixels)")

    background_color = models.CharField(
        max_length=7, 
        blank=True, 
        null=True, 
        help_text="Hex code for background color (e.g., #B91C1C)"
    )
    background_image = models.ImageField(
        upload_to='banners/backgrounds/', 
        blank=True, 
        null=True, 
        help_text="Background image for the banner"
    )
    is_active = models.BooleanField(default=True, help_text="Show this banner on the site")

    # New fields for animated headings
    animated_headings = models.TextField(
        blank=True,
        null=True,
        help_text="Enter animated headings separated by commas (e.g., 'Brochure, Profile, Catalog')"
    )
    heading_text_color = models.CharField(
        max_length=7, 
        default="#FFFFFF", 
        help_text="Hex code for animated heading text color"
    )
    heading_font_size = models.PositiveIntegerField(
        default=24, 
        help_text="Font size for animated headings (in pixels)"
    )
    heading_animation_speed = models.PositiveIntegerField(
        default=100, 
        help_text="Animation speed for headings (in milliseconds per character)"
    )

    def __str__(self):
        return self.title