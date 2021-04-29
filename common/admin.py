from django.contrib import admin
from common.models import(
    Tag,
    Subscriber,
    Blog,
    Comment
)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')
    list_filter = ('title','created_at')
    search_fields = ('title', )



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email','created_at')
    list_filter = ('email','created_at')
    search_fields = ('email', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','short_desc','created_at')
    list_filter = ('title','short_desc','created_at')
    search_fields = ('title','short_desc')

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','comment','created_at')
    list_filter = ('full_name','email','comment','created_at')
    search_fields = ('full_name','email')
# admin.site.register([Subscriber,Blog,Comment])
