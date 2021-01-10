from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category

# Create your views here.
def first(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'images':images, 'locations': locations, 'category':category}
    return render(request, 'home.html', context )


def image_location(request, location):
    images = Image.filter_by_location(location)
    locations = Location.get_locations()
    context = {'images':images,'locations': locations}
    return render(request,'location.html',context)

def search_image(request):
    locations = Location.get_locations()
    if 'searchimage' in request.GET and request.GET["searchimage"]:
        category = request.GET.get("searchimage")
        images = Image.search_by_category(category)
        context = {'images':images,'locations': locations}
        return render(request,'search.html',context)
    else:
        message = "You haven't searched for any term"
        context = {'locations': locations,'message':message}
        return render(request,'search.html',context)
   