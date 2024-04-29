from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    is_published = models.BooleanField(default=False)

    created_year = models.IntegerField(blank=True, null=True)
    created_month = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="70" />'.format(self.image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title
