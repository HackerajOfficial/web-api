

from django.urls import path
from apis.news import views


urlpatterns = [
    path("create/",views.CreateNewsAPIView.as_view()),
    path("",views.ListNewsAPIView.as_view()),
    path("update/<int:pk>/",views.UpdateNewsAPIView.as_view()),
    path("delete/<int:pk>/",views.DeleteAPIView.as_view()),
    path("singlenews/<int:pk>/<str:slug/",views.SingleNewsAPIView.as_view()),
    path("category/",views.category),
]
