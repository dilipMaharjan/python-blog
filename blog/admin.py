from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'slug', 'category', 'created', 'updated')
    list_filter = ('status',)
    search_fields = ('title', 'body')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
