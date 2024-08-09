from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pictures/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=100)
    country = CountryField(blank=True)
    website = models.URLField(max_length=200)

    class Meta:
        db_table = 'user_app_profile_info'
        verbose_name = gettext_lazy('Profile Information')