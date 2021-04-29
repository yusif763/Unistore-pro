from django.contrib import admin
from checkout.models import(
    CheckOut,
    OrderItem,
    Payment
)
# Register your models here.
@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ('reciever','email','phone','city','created_at','completed')
    list_filter = ('city','zip_code','created_at','completed')
    search_fields = ('title','reciever','email','phone','city','completed' )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('author','product','count','created_at','completed')
    list_filter = ('author','product','count','created_at','completed')
    search_fields = ('author','product','count','created_at','completed')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment','created_at')
    list_filter = ('payment','created_at')
    search_fields = ('payment' ,)
