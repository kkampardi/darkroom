from django.contrib import admin

from .models import Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('title', 'slug', 'created', )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Image, ImageAdmin)
