from django.contrib import admin
from .models import Category, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'tags')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('demo_url', 'github_url')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')
