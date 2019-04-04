from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=80)
    url = models.URLField(max_length=300)
    body = models.TextField(max_length=500)
    pub_date = models.DateTimeField()
    vot_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title 

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        return self.body[:100]