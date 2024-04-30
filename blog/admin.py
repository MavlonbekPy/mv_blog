from django.contrib import admin
from blog.models import Post, Img


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')


admin.site.register(Post, PostAdmin)
admin.site.register(Img)
