from django.shortcuts import render
# from apis.accounts.serializer import CreateUserSerializer, UpdateUserSerializer
from apis.accounts.serializer import UserSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import permissions
from apis.accounts.models import User


# class CreateUserAPIView(CreateAPIView):
#     serializer_class    =   CreateUserSerializer
#     permission_classes  =   [permissions.AllowAny]


# class UpdateUserAPIView(UpdateAPIView):
#     serializer_class        =   UpdateUserSerializer
#     queryset                =   User.objects.all()


class CreateUserAPIView(CreateAPIView):
    serializer_class    =   UserSerializer
    permission_classes  =   [permissions.AllowAny]


class UpdateUserAPIView(UpdateAPIView):
    serializer_class        =   UserSerializer
    queryset                =   User.objects.all()



             
