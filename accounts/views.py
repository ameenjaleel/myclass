#import simplejson
#import logging
import json
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from home.models import Classroom,Student
#from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate,get_user_model,logout,login as auth_login
from django.http import HttpResponse
#from home.views import index
from rest_framework.parsers import JSONParser
from django.http import Http404
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
#from home.views import *

def register(request):
    template = 'accounts/register.html'
    return render(request,template)


#@api_view(['POST'])
#@permission_classes((AllowAny,))
def create_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(username=username)
        user.set_password(password)
        user.save()
        return HttpResponse("")

def login(request):
    template = 'accounts/login.html'
    return render(request,template)

#@api_view(['POST'])
#@permission_classes((AllowAny,))
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username
        print password
        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                auth_login(request,user)
                classrooms = Classroom.objects.filter(user=request.user)
                #return HttpResponseRedirect('home/index.html')
                #return render(request, 'home/index.html',{'classrooms': classrooms})
                return HttpResponse("h")
                #return render("home/index.html")
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


def logout_user(request):
    logout(request)
    return render(request,"accounts/login.html")



"""@api_view(['POST'])
@permission_classes((AllowAny,))"""
