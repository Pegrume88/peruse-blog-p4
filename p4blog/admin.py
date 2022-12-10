from django.contrib import admin
from .models import Post, Comment, Category, UserProfile
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(UserProfile)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = 'content'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['name', 'email', 'body']


