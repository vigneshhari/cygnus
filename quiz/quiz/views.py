from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# from django.template.context import RequestContext



def logoutfb(request):
    auth_logout(request)
    return redirect('/')