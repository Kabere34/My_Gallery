from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def image(request):
  return render(request,'gallery_app/index.html')
