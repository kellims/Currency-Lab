from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('currency/', views.CurrencyList.as_view(), name="currency_list"),
    path('currency/new/', views.CurrencyCreate.as_view(), name="currency_create"),
    path('currency/<int:pk>/', views.CurrencyDetail.as_view(), name="currency_detail"),
]