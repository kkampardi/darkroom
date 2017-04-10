from django.contrib import admin

from .models import Upload

# Register your models here.

class UploadAdmin(admin.ModelAdmin):
    model = Upload
    list_display = ('title','image', 'status')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Upload, UploadAdmin)