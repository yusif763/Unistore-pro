from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField
from django.urls import reverse_lazy


User = get_user_model()



class OrderItem(models.Model):

    author = models.ForeignKey(User , verbose_name="User",on_delete=models.CASCADE, 
                                db_index=True,null=True,blank=True, related_name='authorsorder')
    order = models.ForeignKey("CheckOut" , verbose_name="CheckOut",on_delete=models.CASCADE, 
                                db_index=True,null=True,blank=True, related_name='orderwish')
    product  = models.ForeignKey(Product, verbose_name='Product',
                            on_delete=models.CASCADE, db_index=True, related_name='productorders' )

    count = models.IntegerField("Mehsulun Sayi", default=1)
    completed = models.BooleanField(default=False)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return  str(self.count)
# Create your models here.


class Payment(models.Model):



    # information's
    payment = models.CharField("Payment" , max_length=63)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return  self.payment




class CheckOut(models.Model):
    """ 
    This table is for checkouts
    """
    # relation's
    author = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE, 
                                db_index=True,null=True,blank=True, related_name='checkoutusers')
    payment = models.ForeignKey(Payment, verbose_name='Payment',
                                on_delete=models.CASCADE,null=True , blank=True, db_index=True, related_name='payments')
    # information's 
    reciever = models.CharField("Qebul eden" , max_length=67)
    phone = models.CharField("Telefon", max_length=63)
    email = models.EmailField("Email", max_length=63)
    city = models.CharField("Seher" , max_length=63)
    street = models.CharField("Kuce", max_length=127)
    building = models.CharField("Bina", max_length=25)
    zip_code = models.CharField("Zip", max_length=63)
    promo_code = models.CharField("Promo code", max_length=63)
    country = CountryField()
    completed = models.BooleanField(default=False)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'

    def get_absolute_url(self):
        return reverse_lazy('checkout:checkout')

    def __str__(self):
        return  f"{self.id}"
