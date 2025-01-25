from django.contrib import admin
from .models import Picture, Like, Comment


# Register your models here.
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('picture', 'text', 'created_at')

admin.site.register(Like)
