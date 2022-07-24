from django.contrib import admin
from service.models import User

# Register your models here.
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('service_icon','service_title','service_desc')


admin.site.register(User)     #,ServiceAdmin