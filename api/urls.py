from django.urls import path
from .views import ListmenApiView,ListKidsApiView,ListWomenApiView,ClassificationApiView,ListallPrevioseordersApiView,UserCreateAPIView,cartView,checkoutView,ListApiView ,DetailApiView,UpdateApiView ,ListUserchocieApiView ,ItemCreateView,ListPrevioseordersApiView
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib import admin
from django.conf import settings
from api import views

urlpatterns = [
    path('login/',obtain_jwt_token, name='login'),
    path('register/',UserCreateAPIView.as_view(), name='register'),
    path('list/',ListApiView.as_view(),name='list-api'),
    path('list/men/',ListmenApiView.as_view(),name='list-api'),
    path('list/kids/',ListKidsApiView.as_view(),name='list-api'),
    path('list/women/',ListWomenApiView.as_view(),name='list-api'),
    path('cart/',cartView.as_view(),name='cart_api'),
    path('checkout/',checkoutView.as_view(),name='cart_api'),
    path('create/',ItemCreateView.as_view(),name='create-api'),
    path('order/list/',ListPrevioseordersApiView.as_view(),name='orderlist-api'),
    path('order/all/',ListallPrevioseordersApiView.as_view(),name='orderalllist-api'),
    #path('order/create/',OrderCreateView.as_view(),name='createorder-api'),
    path('detail/<int:shop>/',DetailApiView.as_view(),name='Detail-api'),
    path('update/<int:shop>/',UpdateApiView.as_view(),name='update-api'),
    path('classification/',ClassificationApiView.as_view(),name='classification-api'),
]
