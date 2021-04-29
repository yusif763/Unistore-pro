from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True,)
    GENDER_CHOICES = (
        (True, 'Man'),
        (False, 'Woman'),
    )

    image = models.ImageField('Image', upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)
    gender = models.BooleanField('Gender', choices=GENDER_CHOICES, default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    @property
    def profile_picture(self):
        if self.image:
            return self.image
        # return 'https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png'


    def __str__(self):
        return self.email

        