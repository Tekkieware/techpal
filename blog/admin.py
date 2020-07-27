from django.contrib import admin
from .models import User,Post,Question, Reply
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = 'created', 'updated', 'slug'

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ReplyInline,
    ]
    exclude = 'user', 'text', 'slug', 'created', 'replied'
    list_display = ('text', 'user', 'created', 'replied')


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Question, QuestionAdmin)
