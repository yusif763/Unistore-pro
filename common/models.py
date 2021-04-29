from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Tag(models.Model):
    """
    This table is for blogs tags
    """
    title = models.CharField("Title" , max_length=27)

        # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title

class Subscriber(models.Model):
    """
    This table is for subscriber
    """
    #information
    email = models.EmailField('Email', max_length=63)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    """
    This table is for blogs
    """
    #relations
    author = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE, 
                                db_index=True,null=True,blank=True, related_name='blogusers')
    tags = models.ManyToManyField(Tag, verbose_name='Tags',
                                db_index=True,null=True,blank=True, related_name='tags')
    #informations
    image = models.ImageField('Sekil', upload_to='blog_images')
    background = models.ImageField('Sekil',upload_to = 'blog_images' , null = True , blank = True)
    title = models.CharField('Basliq', max_length=127)
    short_desc = models.TextField('Qisa Mezmun', )
    description = models.TextField('Mezmun',null=True,blank=True,)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'

    def __str__(self):
        return  self.short_desc

class Comment(models.Model):
    """
    This table is for comments
    """
    #relations's
    author = models.ForeignKey(User,verbose_name='User',on_delete=models.CASCADE, 
                                db_index=True,null=True,blank=True, related_name='commentusers')
    blog = models.ForeignKey(Blog, verbose_name='Blog',
                                on_delete=models.CASCADE, db_index=True,null=True,blank=True, related_name='blogs')
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_comments', blank=True, null=True)
    #information's
    full_name = models.CharField('Tam ad' , max_length=63)
    email = models.EmailField('Email', max_length=63)
    comment = models.TextField('Rey', )

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Koment'
        verbose_name_plural = 'Komentler'

    def __str__(self):
        return  self.comment
