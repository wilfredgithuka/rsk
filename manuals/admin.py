from django.contrib import admin
from .models import Manuals
#from django_summernote.admin import SummernoteModelAdmin

#Configure how manuals are displayed on admin page


class ManualsAdmin(admin.ModelAdmin):
    list_display = ('title','description','format','updated_on', 'created_on')
    #list_filter = ("title")
    #search_fields = ['title', 'description']
#    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Manuals, ManualsAdmin)
