from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('index/', views.index),
    path('test/', views.test),
    path('products/', views.products, name='products'),
    path('cars/', views.CarsListView.as_view(), name='cars')
]
