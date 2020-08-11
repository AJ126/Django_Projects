from django.contrib import admin
from testapp.models import *
# Register your models here.
class dataAdmin(admin.ModelAdmin):
    list_display=['name','contact','address','order','status']
admin.site.register(data,dataAdmin)

class feedbackAdmin(admin.ModelAdmin):
    list_display=['name','feedback']
admin.site.register(feedback,feedbackAdmin)    
