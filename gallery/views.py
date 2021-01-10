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