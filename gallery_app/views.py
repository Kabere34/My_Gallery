from django.http import HttpResponse
from django.shortcuts import render
from .models import Images


# Create your views here.
def homepage(request):
  images=Images.get_all_images()
  return render(request,'gallery_app/index.html',{'images':images})


