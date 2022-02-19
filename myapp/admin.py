from django.contrib import admin
from .models import File
# Register your models here.
@admin.register(File)
class UserAdmin(admin.ModelAdmin):
    list_display=('name','image','videofile')