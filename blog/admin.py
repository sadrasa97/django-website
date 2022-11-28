from django.contrib import admin

# Register your models here.
from blog.models import Post,Category
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_at'
    empty_value_display='-empty-'
    list_display=('title','author','counted_views','status','publish_date','created_at')
    list_filter=('status','author')
    ordering=['created_at']
    search_feilds=['title','content']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)

