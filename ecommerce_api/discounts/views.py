# discounts/views.py
from rest_framework import generics
from .models import Discount
from .serializers import DiscountSerializer

class DiscountCreateView(generics.CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountCancelView(generics.DestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class DiscountListView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer