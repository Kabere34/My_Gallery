from django.test import TestCase
from .models import Images,Category,Location
# Create your tests here.
class Images(TestCase):
   def setUp(self):
     self.location = Location(name = "Nairobi")

     self.image=Images(image_name = "test",image_description = "test description",location = self.location)
   def test_instance(self):
    self.assertTrue(isinstance(self.test,Images))



