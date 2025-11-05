from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'rating', 'is_active', 'created_at')
    list_filter = ('rating', 'is_active', 'created_at')
    search_fields = ('name', 'designation', 'message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'designation', 'image')
        }),
        ('Testimonial Content', {
            'fields': ('message', 'rating')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request)
