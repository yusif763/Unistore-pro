from django.db import models
from checkout.models import *
from django.contrib.auth import get_user_model
from slugify import slugify
import random
# Create your models here.

User = get_user_model()



class Tag(models.Model):
    """ 
    This table is for tags
    """
    tags = models.CharField('taglar',max_length=60)
    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.tags 

class Category(models.Model):
    """
    This table is for product's categories
    """
    # information's
    types = models.CharField('kateqoriya',max_length=60)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return  self.types 


class Brands(models.Model):
    """
    This table is for models brand 
    """
    # information's
    brand = models.CharField("Brand" , max_length=25)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return  self.brand

class ScreenSize(models.Model):
    """
    This table is for product screen size 
    """
    # information's
    size = models.CharField('Ekran olcusu' , max_length=10)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ekran olcusu'
        verbose_name_plural = 'Ekran olculeri'

    def __str__(self):
        return  self.size

class Product(models.Model):
    """
    This table is for Products names price ...
    """
    #relation's
    category = models.ForeignKey(Category, verbose_name='Category',
                                on_delete=models.CASCADE, db_index=True, related_name='categories')
    brand = models.ForeignKey(Brands, verbose_name='Brands',
                                on_delete=models.CASCADE, db_index=True, related_name='brands')
    screensize = models.ManyToManyField(ScreenSize, verbose_name='ScreenSize',
                                db_index=True, related_name='screensizes')
    taglar = models.ManyToManyField(Tag, verbose_name='Taglar',
                                db_index=True, related_name='taglar' , blank=True , null=True)
    #information's
    short_title = models.CharField('Mehsulun adi' ,max_length=127)
    price = models.DecimalField('Qiymet' , max_digits=30 , decimal_places=2)
    faiz = models.IntegerField("Endirim Faizi", null = True , blank= True)
    slug = models.SlugField('Slug', max_length=155, editable=False, blank=True, null= True)
    full_title = models.CharField('Mehsulun tam adi', max_length=255)
    description = models.TextField('Melumat', )
    main_image = models.ImageField(' Esas Sekil', upload_to='products_main_images', null = True)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        random1 = random.randint(0, 100)
        self.slug = f'{slugify(self.full_title)}-{random1}'
        return super(Product, self).save(*args, **kwargs)

    @property
    def endirim(self):
        if self.faiz:
            son_qiymet = self.price - (self.price * self.faiz)/100
            return round(son_qiymet,2)
         
    class Meta:
        verbose_name = 'Mehsul'
        verbose_name_plural = 'Mehsullar'

    def __str__(self):
        return  self.full_title


class ShortSpec(models.Model):
    #relation's
    product =models.ManyToManyField(Product, verbose_name='Product',
                                    db_index=True, related_name='shortspecs',null=True , blank= True)
    #information's
    short_specs = models.CharField('Qisa xususiyyetler' , max_length=63, null= True , blank= True)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Qisa Xususiyyet'
        verbose_name_plural = 'Qisa xususiyyetler'

class Image(models.Model):
    """
    This table is for Products images ...
    """
    #relation's
    product = models.ForeignKey(Product, verbose_name='Product',
                                on_delete=models.CASCADE, db_index=True, related_name='productimages')
    #information's
    image = models.ImageField('Sekil', upload_to='product_images', null = True , blank=True )
    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sekil'
        verbose_name_plural = 'Sekiller'



class ProductSpecName(models.Model):
    """
    This table is for specifations names like : 'operating system' , 'processor'
    """
    #relation's
    category = models.ManyToManyField(Category, verbose_name='Category',
                                 db_index=True, related_name='categoryspec',null=True , blank= True)
    #information's
    title = models.CharField('Xususiyyetin adi' ,max_length=127)


    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mehsulun xususiyyet adi'
        verbose_name_plural = 'ehsulun xususiyyet adlari'

    def __str__(self):
        return  self.title



class ProductSpecDesc(models.Model):
    """
    This table is for specifations description like :'windows 10'
    """
    product = models.ForeignKey(Product, verbose_name='Product',
                                on_delete=models.CASCADE, db_index=True, related_name='productnames')
    prod_spec_name = models.ForeignKey(ProductSpecName, verbose_name='Product Spec Name',
                                on_delete=models.CASCADE, db_index=True, related_name='prod_names')
    # information's
    desc = models.TextField("Xusisiyyeti yazin")

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mehsulun xususiyyeti'
        verbose_name_plural = 'ehsulun xususiyyetleri'

    def __str__(self):
        return  self.desc



class Review(models.Model):
    """
    This table is for comments
    """
    #relation's
    author = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE, 
                                db_index=True,null=True,blank=True, related_name='reviewusers')
    product = models.ForeignKey(Product, verbose_name='Product',
                                on_delete=models.CASCADE, db_index=True, related_name='productsreview')
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_reviews', blank=True, null=True)

    #information's

    full_name = models.CharField('Tam ad' , max_length=63)
    email = models.EmailField('Email', max_length=63)
    comment = models.TextField('Rey', )    
    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return  self.comment