from django.contrib import admin
from devmanage.models import Ip,Device
# Register your models here.
class IpAdmin(admin.ModelAdmin):
    list_display = ('ipaddr','hostname','ostype','ports','application','status')
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('ipaddr','cpu','memory','location','product','platform','sn')


admin.site.register(Ip,IpAdmin)
admin.site.register(Device,DeviceAdmin)
