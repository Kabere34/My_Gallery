from django.http import HttpResponse
from django.shortcuts import render
from .models import Images


# Create your views here.
def homepage(request):
  images=Images.get_all_images()
  return render(request,'gallery_app/index.html',{'images':images})

def search_results(request):
  if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Images.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'gallery_app/search.html',{'message':message, 'images':searched_images})
  else:
    message = "You haven't searched for any term"
    return render(request,'gallery_app/search.html',{'message':message})

# def view_image(request,id):
#   product=Images.objects.filter(id=id).first()
#   return render(request,'')

