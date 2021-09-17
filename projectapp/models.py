from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="picture")
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
