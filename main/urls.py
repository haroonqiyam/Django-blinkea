
from django.urls import path
from . import views  # Import views from the same app
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('page/<slug:slug>/', views.page_detail, name='page_detail'),  # Individual page view
    path('solutions/', lambda request: render(request, 'main/solutions.html'), name='solutions'),
    path('services/', lambda request: render(request, 'main/services.html'), name='services'),
    path('howitworks/', lambda request: render(request, 'main/howitworks.html'), name='howitworks'),
    path('faqs/', lambda request: render(request, 'main/faqs.html'), name='faqs'),
    path('pricing/', lambda request: render(request, 'main/pricing.html'), name='pricing'),
    path('examples/', lambda request: render(request, 'main/examples.html'), name='examples'),
    path('refundpolicy/', lambda request: render(request, 'main/refundpolicy.html'), name='refundpolicy'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)