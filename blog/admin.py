from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'published_at', 'created_at')
    list_filter = ('published', 'published_at', 'author')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_at',)
    date_hierarchy = 'published_at'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Publication', {
            'fields': ('published', 'published_at', 'author')
        }),
        ('Tags', {
            'fields': ('tags',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author')
