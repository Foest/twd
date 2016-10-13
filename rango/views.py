from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "Rango says hello world!" + '</br><a href="/rango/about">About</a>'
    return HttpResponse(html)

def default(request):
    return HttpResponse("This is the default page!")

def about(request):
    html = "This is the Rango \'about\' page!" + '</br><a href="/rango/">Index</a>'
    return HttpResponse(html)
