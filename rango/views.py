from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

def default(request):
    return HttpResponse("This is the default page!")

def about(request):
    html = "This is the Rango \'about\' page!" + '</br><a href="/rango/">Index</a>'
    return HttpResponse(html)
