from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.index , name='index'),
    url(r'loginpage',views.login , name='login'),
    url(r'signuppage',views.signup , name='signup'),
    url(r'login',views.loginprocess , name = 'loginprocess'),
    url(r'signup',views.signupprocess , name = 'signupprocess'),
    url(r'verified',views.verified , name = 'verified'),
    url(r'forpass' , views.forpass , name='forpass'),
	url(r'change' , views.change , name='change'),
	url(r'sendvericode' , views.sendveri , name='sendveri'),
    url(r'logout' , views.logout , name='logout'),

    ]
