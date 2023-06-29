from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('currency/', views.CurrencyList.as_view(), name="currency_list"),
    path('currency/new/', views.CurrencyCreate.as_view(), name="currency_create"),
    path('currency/<int:pk>/', views.CurrencyDetail.as_view(), name="currency_detail"),
    path('currency/<int:pk>/update',views.CurrencyUpdate.as_view(), name="currency_update"),
    path('currency/<int:pk>/delete',views.CurrencyDelete.as_view(), name="currency_delete"),
    path('currency/<int:pk>/money/new/', views.MoneyCreate.as_view(), name="money_create")
]