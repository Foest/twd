from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def default(request):
    return HttpResponse("This is the default page!")

def about(request):
    context_dict = {'h2': "I am an h2!"}
    return render(request, 'rango/about.html', context_dict)
