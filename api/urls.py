from django.urls import path
from .views import UserCreateAPIView ,ListApiView ,DetailApiView,UpdateApiView
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.conf import settings
from api import views

urlpatterns = [
    path('login/',obtain_jwt_token, name='login'),
    path('register/',UserCreateAPIView.as_view(), name='register'),
    path('list/',ListApiView.as_view(),name='list-api'),
    path('detail/<int:shop>/',DetailApiView.as_view(),name='Detail-api'),
    path('update/<int:shop>/',UpdateApiView.as_view(),name='update-api'),


]

