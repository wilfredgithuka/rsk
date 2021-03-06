from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

## Configure how posts are displayed on admin page

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)

#class PostAdmin(admin.ModelAdmin):
#    list_display = ('title', 'slug', 'status','created_on')
#    list_filter = ("status",)
#    search_fields = ['title', 'content']
#    prepopulated_fields = {'slug': ('title',)}

#admin.site.register(Post, PostAdmin)

# Register your models here.
