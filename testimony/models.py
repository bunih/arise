from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


User=settings.AUTH_USER_MODEL

# Create your models here.
SOURCE_CHOICE=[
    ('church','from Church'),
    ('online','from Online'),
    ]
LEVEL_CHOICE=[
    ('low','Lower'),
    ('normal','Normal level'),
    ('hero','Hero Level'),
    ('high','High Level'),
    ]
GENDER_CHOICE=[
    ('male','MALE GENDER'),
    ('female','FEMALE GENDER'),
    ]

class Location(models.Model):
    name=models.CharField(max_length=255)
    country=models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.country} | {self.name}"



class Believer(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name='testimonies',blank=True,null=True)
    
    @property
    def get_full(self,*args,**kwargs):
        return  f"{self.name}"

    def __str__(self) -> str:
        return f"{self.get_full}"


class Testimony(models.Model):
    slug=models.SlugField(blank=True,null=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    believer=models.ForeignKey(Believer,on_delete=models.CASCADE,related_name='testimonies',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,related_name='testimonies',blank=True,null=True)
    source=models.CharField(max_length=10,choices=SOURCE_CHOICE)
    category=models.CharField(max_length=10,choices=LEVEL_CHOICE)
    witness=models.CharField(max_length=255,blank=True,null=True)
    witness_number=models.CharField(max_length=255,blank=True,null=True)
    allowed=models.BooleanField(default=True)
    file=models.FileField(upload_to=f'testimonies/%Y/%m/')
    thumbnail=models.ImageField(upload_to=f'testimonies/%Y/%m/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True,null=True)
    uploaded_at=models.DateTimeField(blank=True,null=True)

    def __str__(self) -> str:
        return f"{self.title}"



    def get_absolute_url(self):
        return reverse('testimony:show',kwargs={'slug':self.slug})


    def action(self):
        return reverse('administrator:action_testimony',kwargs={'slug':self.slug})

    def save(self,*args,**kwargs):
        if not self.pk:
           self.slug=slugify(self.title)
        super().save(*args,**kwargs)



    class Meta:
        db_table='testimonies'