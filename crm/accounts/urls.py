from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('customer/', views.customer),
    path('products/', views.products),
]
