from django.conf.urls import url
from dem import views

app_name = 'dem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
]
