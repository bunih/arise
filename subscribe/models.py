from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='subscribers'

    def __str__(self):
        return self.email