from django.shortcuts import render, get_object_or_404
# from apis.accounts.serializer import CreateUserSerializer, UpdateUserSerializer
from apis.accounts.serializer import UserSerializer, UserNewsSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework import permissions
from apis.accounts.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apis.news.models import News
from rest_framework import status
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



@api_view(['GET'])
def UserPosts(request, *args, **kwargs):
    user_id     =   kwargs.get('pk')
    user        =   get_object_or_404(User, pk=user_id)
    serializer = UserNewsSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

             
