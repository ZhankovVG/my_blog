from django.contrib import admin
from .models import Post, Comments


admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titlee', 'author')
    

admin.site.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
