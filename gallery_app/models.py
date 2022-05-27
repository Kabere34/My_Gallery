from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length =30)

class Category(models.Model):
  name = models.CharField(max_length =30)
  category_list=[]

class Images(models.Model):
  image_name=models.CharField(max_length=30)
  image_description=models.CharField(max_length=200)
  gallery_image = models.ImageField(upload_to = 'articles/', unique=True)
  category = models.ManyToManyField(Category)
  location = models.ForeignKey(Location,on_delete=models.CASCADE)







