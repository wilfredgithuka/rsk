from django.contrib import admin
from .models import Operator


class OperatorAdmin(admin.ModelAdmin):
    list_display = ('call_sign', 'name', 'address','telephone','created_on','status')
    list_filter = ("status",)
    search_fields = ['call_sign', 'name']
    prepopulated_fields = {'name': ('address',)}
  
admin.site.register(Operator, OperatorAdmin)
#admin.site.register(Ham_Operator)
# Register your models here.
