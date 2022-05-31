from django.test import TestCase
from .models import Images,Category,Location
# Create your tests here.
class ImagesTestClass(TestCase):
   def setUp(self):
     self.image_location = Location(name = "Nairobi")
     self.image_location.save_location()
     self.gallery_image=Images(image_name = "test",image_description = "test description",image_location = self.location)

   def test_instance(self):
    self.assertTrue(isinstance(self.image,Images))

   def test_save_image(self):
        self.gallery_image.save_image()
        self.images = Images.objects.all()
        self.assertTrue(len(self.images) > 0)

   def test_get_image_by_id(self):
        self.image.save_image()
        self.image = Images.get_image_by_id(1)
        self.assertTrue(isinstance(self.image,Images))

   def test_update_image(self):
        self.image.save_image()
        self.image = Images.objects.filter(id = 1).update(galler_image = "/image")
        self.updated_image = Images.get_image_by_id(1)
        self.assertEqual(self.updated_image.gallery_image,"/image")

   def test_search_by_category(self):
        self.image.save_image()
        self.category = Category(name = "test")
        self.category.save_category()
        self.image = Images.get_image_by_id(1).Category.add(self.category)
        self.searched_images = Images.search_by_category('test')
        self.assertTrue(len(self.searched_images) > 0)

   def test_search_by_location(self):
        self.image.save_image()
        self.searched_images = Images.search_by_location('Nairobi')
        self.assertTrue(len(self.searched_images) > 0)

   def test_delete_image(self):
        self.image.save_image()
        self.searched_image = Images.get_image_by_id(1)
        self.searched_image.delete_image()
        self.assertTrue(len(Images.objects.all()) == 0)








