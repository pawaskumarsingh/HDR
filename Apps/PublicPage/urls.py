from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('p/<slug:slug>/', views.property_detail, name='property_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.media_page, name='media'),
    path('nri/', views.nri_page, name='nri'),
    path('career/', views.career_page, name='career'),
]