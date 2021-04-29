from django.contrib import admin
from contact.models import(
    Contact
)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','message','email','created_at')
    list_filter = ('full_name','email')
    search_fields = ('full_name','email')

# admin.site.register([Contact])
# Register your models here.
