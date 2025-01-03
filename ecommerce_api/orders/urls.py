# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order-list'),  # No need for 'orders/' prefix here
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('cancel/', views.OrderCancelView.as_view(), name='order-cancel'),
]
