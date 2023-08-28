from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "pub_date", "author", "tag")
    fields = ("title", "slug", "description", "content", "image", "pub_date", "author", "tag")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("pub_date",)
    search_fields = ("title",)
    ordering = ("-title",)
