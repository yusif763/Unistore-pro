from django.contrib import admin
from favorites.models import *
# Register your models here.
@admin.register(WishList)
class WishList(admin.ModelAdmin):
    list_display = ('user',"product",'created_at')
    list_filter = ('user',"product")
    search_fields = ('user',"product")