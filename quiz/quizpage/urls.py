from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$' , views.index , name='index'),
	url(r'dash', views.dash, name='dash'),
	url(r'attempted' , views.attempted , name='attempted'),
	url(r'avaliable' , views.avaliable , name='avaliable'),
	url(r'attempt' , views.attempt , name='attempt'),
	url(r'quizvalidate' , views.validate , name='validate'),
	url(r'rank' , views.rank , name='rank'),
    ]

    