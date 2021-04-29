from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    This table is for contact page 
    """
    #information's
    full_name = models.CharField("Tam ad" , max_length=63)
    message = models.TextField("Message",)
    email = models.EmailField('Email',max_length=63)


    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)