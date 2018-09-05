from django.conf.urls import url
from . import views

urlpatterns = [
    # index method
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)/$', views.details, name='details')

]
