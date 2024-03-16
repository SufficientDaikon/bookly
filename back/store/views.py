from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import *

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'status': 'error', 'message': 'Invalid username or password.'})
    return Response({'status': 'error', 'message': 'Invalid request method.'})


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, password=password)
            user.save()
            return Response({'status': 'success'})
        except IntegrityError:
            return Response({'status': 'error', 'message': 'Username already exists.'})
    return Response({'status': 'error', 'message': 'Invalid request method.'})
        