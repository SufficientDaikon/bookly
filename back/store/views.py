from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Redirect to login page after successful registration
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            except IntegrityError:
                return Response({"status": "erorr", "message": "username already exists"})
    return Response({'status': 'error', 'message': 'Invalid request method.'})
