from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    message = models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name
