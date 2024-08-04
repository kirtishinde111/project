from .models import UploadFile
from django.contrib import admin

@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
