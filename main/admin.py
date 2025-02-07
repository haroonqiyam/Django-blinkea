from django.contrib import admin
from .models import NavLink, Section, FooterLink
from .models import CTASection, Page, HeaderSettings, Banner, HeroSection, Client, ClientSettings, Portfolio, PortfolioSettings, ScrollPortfolioConfig, ScrollLogo, ScrollThumbnail


# Scroll Portfolio Configuration
@admin.register(ScrollPortfolioConfig)
class ScrollPortfolioConfigAdmin(admin.ModelAdmin):
    list_display = ['background_color', 'logo_scroll_speed', 'logo_width', 'thumbnail_scroll_speed', 'thumbnail_width']
    list_editable = ['logo_scroll_speed', 'logo_width', 'thumbnail_scroll_speed', 'thumbnail_width']
    fieldsets = (
        ('Background Settings', {
            'fields': ('background_color',),
        }),
        ('Logo Panel Settings', {
            'fields': ('logo_scroll_speed', 'logo_width'),
        }),
        ('Thumbnail Panel Settings', {
            'fields': ('thumbnail_scroll_speed', 'thumbnail_width'),
        }),
    )
    help_texts = {
        'background_color': "CSS background property value (e.g., 'linear-gradient(to right, navy, purple)' or '#ffffff').",
        'logo_scroll_speed': "Speed of the logo scrolling (in seconds). Lower values mean faster scrolling.",
        'thumbnail_scroll_speed': "Speed of the thumbnail scrolling (in seconds). Lower values mean faster scrolling.",
        'logo_width': "Width of each logo in pixels.",
        'thumbnail_width': "Width of each thumbnail in pixels.",
    }


# Scroll Logo
@admin.register(ScrollLogo)
class ScrollLogoAdmin(admin.ModelAdmin):
    list_display = ['image', 'alt_text']
    search_fields = ['alt_text']
    list_per_page = 20  # Pagination for logos


# Scroll Thumbnail
@admin.register(ScrollThumbnail)
class ScrollThumbnailAdmin(admin.ModelAdmin):
    list_display = ['image', 'link', 'alt_text']
    search_fields = ['alt_text', 'link']
    list_per_page = 20  # Pagination for thumbnails
    

# Re Arrange Home page
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "template_name":
            kwargs['choices'] = [
                ('main/banner.html', 'Banner'),
                ('main/scrollportfolio.html', 'Scroll Panel'),
                ('main/hero.html', 'Hero'),
                ('main/clients.html', 'Clients & Partners'),
                ('main/portfolio.html', 'Portfolio'),
                ('main/cta.html', 'Call to Action'),
            ]
        return super().formfield_for_choice_field(db_field, request, **kwargs)


# CTA call to action
class CTASectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text', 'button_url')  # Add button_url to the displayed fields
    fields = ('title', 'title_color', 'title_size', 'title_alignment', 
              'container_height', 'bg_color_start', 'bg_color_end', 
              'padding_top', 'padding_bottom', 'padding_left', 'padding_right', 
              'button_text', 'button_text_color', 'button_color', 
              'button_width', 'button_url')  # Make sure button_url is included in the fields

admin.site.register(CTASection, CTASectionAdmin)

# Portfolio Model
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title",)
    ordering = ("order",)

# portfolio setting

@admin.register(PortfolioSettings)
class PortfolioSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "section_title",
        "columns",
        "container_background_color",
        "container_spacing_top",  # Corrected field name
        "container_spacing_bottom",  # Corrected field name
        "container_spacing_left",  # Corrected field name
        "container_spacing_right",  # Corrected field name
        "item_height",
    )
    fieldsets = (
        (None, {
            "fields": (
                "section_title",
                "columns",
            )
        }),
        ("Container Styling", {
            "fields": (
                "container_background_color",
                "container_spacing_top",
                "container_spacing_bottom",
                "container_spacing_left",
                "container_spacing_right",
            )
        }),
        ("Portfolio Item Settings", {
            "fields": ("item_height",)
        }),
    )


# Client List
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name",)

@admin.register(ClientSettings)
class ClientSettingsAdmin(admin.ModelAdmin):
    list_display = ("columns", "container_spacing_top", "container_spacing_bottom")


# Hero Section with Gradient BG
@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_active')
    list_filter = ('is_active',)


# Red Banner
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'background_color')
    fieldsets = (
        (None, {
            'fields': (
                'title', 'subtitle', 'image', 'button_text', 'button_link',
                'background_color', 'background_image', 'is_active',
            )
        }),
        ('Spacing', {
            'fields': (
                'title_spacing_top', 'title_spacing_bottom',
                'subtitle_spacing_top', 'subtitle_spacing_bottom',
                'image_spacing_top', 'image_spacing_bottom',
                'button_spacing_top', 'button_spacing_bottom',
            )
        }),
        ('Animated Headings', {
            'fields': (
                'animated_headings', 'heading_text_color', 
                'heading_font_size', 'heading_animation_speed',
            )
        }),
    )

    

# Pages CMS for top menu
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'slug')



admin.site.register(Page, PageAdmin)
admin.site.register(NavLink)
admin.site.register(FooterLink)


# Registering HeaderSettings in the Django admin
@admin.register(HeaderSettings)
class HeaderSettingsAdmin(admin.ModelAdmin):
    list_display = (
        'background_color', 'logo_height', 'header_height',
        'button_text', 'button_background_color', 'button_text_color',
        'container_top_padding', 'container_bottom_padding', 'container_left_padding', 'container_right_padding'
    )
    search_fields = ['background_color', 'button_text']

    # Optionally, add reset functionality
    actions = ['reset_header_settings']

    def reset_header_settings(self, request, queryset):
        for header_setting in queryset:
            header_setting.reset_to_default()
        self.message_user(request, "Header settings reset to default values.")
    reset_header_settings.short_description = "Reset Header Settings to Default"