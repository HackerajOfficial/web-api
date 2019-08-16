from django.shortcuts import render
from apis.news.serializer import NewsSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from apis.news.models import News
from rest_framework import permissions
from common.permissions import IsAdminOrJournalist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apis.news.models import News
from rest_framework import status
from rest_framework_simplejwt import authentication
from common.pagination  import NewsPaginator




class CreateNewsAPIView(CreateAPIView):
    serializer_class        =   NewsSerializer
    # permission_classes      =   [permissions.IsAuthenticated]
    permission_classes      =   [IsAdminOrJournalist]

@api_view(['GET']) #functional view
def category(request):
    categories     =    dict(News.CATEGORY)
    return Response(categories, status=status.HTTP_200_OK)

class UpdateNewsAPIView(UpdateAPIView):
    authentication_classes  =   [authentication.JWTAuthentication]
    serializer_class        =   NewsSerializer
    permission_classes      =   [IsAdminOrJournalist]
    queryset                =   News.objects.all()
    

class DeleteAPIView(DestroyAPIView):
    authentication_classes      =   [authentication.JWTAuthentication]
    permission_classes          =   [IsAdminOrJournalist]
    queryset                    =   News.objects.all()

class SingleNewsAPIView(RetrieveAPIView):
    serializer_class            =   NewsSerializer
    permission_classes          =   [permissions.AllowAny]
    queryset                    =   News.objects.all()
    lookup_fields               =   ['pk','slug']


class ListNewsAPIView(ListAPIView):
    serializer_class            =   NewsSerializer
    permission_classes          =   [permissions.AllowAny]
    queryset                    =   News.objects.all()
    pagination_class            =   NewsPaginator