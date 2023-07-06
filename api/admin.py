from django.contrib import admin
from .models import BookModel,AuthorModel
# Register your models here.


@admin .register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ("id","full_name")
    search_fields = ("full_name",)
    list_filter = ("created_at","update_at")


@admin .register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ("id","title",)
    list_display_links = ("id", "title",)
    search_fields = ("full_name",)
    list_filter = ("created_at","update_at",)