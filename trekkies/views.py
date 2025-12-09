from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def trekkie_blog(request):
    return HttpResponse("Hello, trekkies - welcome to the blog to discuss all things Star Trek!")
