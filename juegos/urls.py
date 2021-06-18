from django.conf.urls import url
from juegos import views


urlpatterns = [
    url(r'^juegos/$', views.juego_list),
    url(r'^juegos/(?P<pk>[0-9]+)/$', views.juego_detail),
]