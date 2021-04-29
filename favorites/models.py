from django.db import models
from product.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class WishList(models.Model):
    """
    This table is for Wish List ...
    """
    #relation's
    user = models.ForeignKey(User, verbose_name='User',
                            on_delete=models.CASCADE, db_index=True, related_name='wishusers', null= True , blank=True)
    product = models.ForeignKey(Product, verbose_name='Product',
                            on_delete=models.CASCADE, db_index=True, related_name='wishproducts', null= True , blank=True)
    #information's
   

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mehsul'
        verbose_name_plural = 'Mehsullar'
