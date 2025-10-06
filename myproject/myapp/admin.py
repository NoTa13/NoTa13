from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # <-- здесь ошибка
    ordering = ('created_at',)  # <-- и здесь ошибка

admin.site.register(Post, PostAdmin)
