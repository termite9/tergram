from django.contrib import admin
from posts.models import Post, PostImage, Comment,HashTag
import admin_thumbnails
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple


class CommentInline(admin.TabularInline):
    model=Comment
    extra=1
class PostImageInline(admin.TabularInline):
    model=PostImage
    extra=1

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
    ]
    formfield_overrides = {
        ManyToManyField: {"widget" : CheckboxSelectMultiple},
    }

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "photo",
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "content",
    ]

@admin_thumbnails.thumbnail("photo")
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    pass
