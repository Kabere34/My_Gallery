from email.mime import image
from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length =30)

  def save_location(self):
    self.save()

  def delete_location(self):
    self.delete

  def __str__(self):
    return self.name


class Category(models.Model):
  name = models.CharField(max_length =30)

  def save_category(self):
    self.save()

  def delete_category(self):
    self.save()

  def __str__(self):
    return self.name

class Images(models.Model):
  image_name=models.CharField(max_length=30)
  image_description=models.CharField(max_length=200)
  gallery_image = models.ImageField(upload_to = 'gallery/', null=True)
  image_category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
  image_location = models.ForeignKey(Location,on_delete=models.CASCADE, blank=True, null=True)

  def save_images(self):
    self.save()

  def delete_images(self):
    self.delete

  def __str__(self):
    return self.image_name

  # def test_Instance():




  @classmethod
  def get_all_images(cls):
    images=cls.objects.all()
    return images

  @classmethod
  def search_by_category(cls,search_term):
      images = cls.objects.filter(image_category__name__icontains=search_term)
      return images

  @classmethod
  def search_by_location(cls,search_term):
      location = Location.objects.get(name=search_term)
      images=cls.objects.filter(location =location)
      return images

  @classmethod
  def view_image_by_id(cls,id):
    image=cls.objects.get(id=id)
    return image








