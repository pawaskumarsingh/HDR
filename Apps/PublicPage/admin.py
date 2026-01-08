from django.contrib import admin
from .models import Property, PropertyImage, PropertyInquiry

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'property_type', 'is_featured')
    list_filter = ('property_type', 'is_featured', 'created_at')
    search_fields = ('title', 'location')
    inlines = [PropertyImageInline]
    prepopulated_fields = {'slug': ('title',)}

@admin.register(PropertyInquiry)
class PropertyInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'property', 'created_at')
    search_fields = ('name', 'email', 'message')
