from django.conf.urls import url
from dem import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
