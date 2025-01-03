from django.urls import path
from .views import DiscountCreateView, DiscountCancelView, DiscountListView

urlpatterns = [
    path('', DiscountListView.as_view(), name='discount-list'),  # Root URL for /api/discounts/
    path('create/', DiscountCreateView.as_view(), name='discount-create'),
    path('cancel/', DiscountCancelView.as_view(), name='discount-cancel'),
]
