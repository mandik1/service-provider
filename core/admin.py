from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(Services)
admin.site.register(Appointement)
admin.site.register(Userdata)
admin.site.register(PaymentMode)


class MyAdmin(admin.ModelAdmin):
    list_display = ('servicename','image','price',)
