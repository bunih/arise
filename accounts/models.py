from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=10, default='Active')
    phone = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    ref_number = models.CharField(max_length=100, blank=True, null=True)
    sirname = models.CharField(max_length=100, blank=True, null=True)
    profile = models.ImageField(
        upload_to="images/users", default='/images/default/profile/logo.png')

    def __str__(self):
        return f'{self.user}'


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username