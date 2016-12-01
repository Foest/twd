from django.conf.urls import url
from dem import views

app_name = 'dem'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^interact_test/$', views.interact_test, name='interact_test'),
    url(r'^my_assignments/$', views.my_assignments, name='my_assignments'),
    url(r'^show_mission/(?P<mission_name_slug>[\w\-]+)/$',
        views.show_mission, name='show_mission'),
]
