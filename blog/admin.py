from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status']
    actions = ['make_draft', 'make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))

    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{} sucessfully marked as Draft'.format(updated_count))
    make_draft.short_description = 'Mark selected stories as Draft'

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} sucessfully marked as published'.format(updated_count))
    make_published.short_description = 'Mark selected stories as published'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']