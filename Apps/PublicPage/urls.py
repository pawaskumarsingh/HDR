from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('properties/<slug:slug>/', views.property_detail, name='property_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('media/', views.media_page, name='media'),
    path('nri/', views.nri_page, name='nri'),
    path('career/', views.career_page, name='career'),
]
