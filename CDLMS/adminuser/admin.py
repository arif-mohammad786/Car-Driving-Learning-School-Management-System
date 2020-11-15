from django.contrib import admin
from .models import admin_model
# Register your models here.
@admin.register(admin_model)
class admin_admin(admin.ModelAdmin):
    list_display=['id','username','password']