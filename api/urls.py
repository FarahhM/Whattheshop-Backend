from django.urls import path
from .views import UserCreateAPIView ,ListApiView ,DetailApiView,UpdateApiView ,ListUserchocieApiView ,ItemCreateView,OrderCreateView,ListPrevioseordersApiView
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.conf import settings
from api import views

urlpatterns = [
    path('login/',obtain_jwt_token, name='login'),
    path('register/',UserCreateAPIView.as_view(), name='register'),
    path('list/',ListApiView.as_view(),name='list-api'),
    path('create/',ItemCreateView.as_view(),name='create-api'),
    path('order/list/',ListPrevioseordersApiView.as_view(),name='orderlist-api'),
    path('order/create/',OrderCreateView.as_view(),name='createorder-api'),
    path('detail/<int:shop>/',DetailApiView.as_view(),name='Detail-api'),
    path('update/<int:shop>/',UpdateApiView.as_view(),name='update-api'),


]

