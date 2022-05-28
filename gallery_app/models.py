from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length =30)
  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length =30)
  def __str__(self):
    return self.name

class Images(models.Model):
  image_name=models.CharField(max_length=30)
  image_description=models.CharField(max_length=200)
  gallery_image = models.ImageField(upload_to = 'gallery/', null=True)
  image_category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
  image_location = models.ForeignKey(Location,on_delete=models.CASCADE, blank=True, null=True)

  def save_image(self):
    self.save()
  @classmethod
  def get_all_images(cls):
    images=cls.objects.all()
    return images







