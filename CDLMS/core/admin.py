from django.contrib import admin
from .models import packagemodel,applicants_model
# Register your models here.
@admin.register(packagemodel)
class adminpackagemodel(admin.ModelAdmin):
    list_display=['id','pname','pdesc','pduration','pprice']

@admin.register(applicants_model)
class admin_applicant_model(admin.ModelAdmin):
    list_display=['id','package','start_date','timing','name','email','phone','gender','age','licenseno','licensepic','address','status']