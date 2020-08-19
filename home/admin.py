from django.contrib import admin

from .models import HomeItems

class HomeItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'box1', 'box2', 'image')

admin.site.register(HomeItems, HomeItemsAdmin)
