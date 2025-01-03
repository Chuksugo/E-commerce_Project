from rest_framework import generics, filters , permissions, status
from .models import Product, Review, Category, ProductImage
from .serializers import ProductSerializer, ReviewSerializer, CategorySerializer, ProductImageSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    in_stock = django_filters.BooleanFilter(field_name='stock_quantity', lookup_expr='gt')

    class Meta:
        model = Product
        fields = ['category', 'price_min', 'price_max', 'in_stock']

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter  # Use the filter class
    search_fields = ['name'] 

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        in_stock = self.request.query_params.get('in_stock', None)

        try:
            if min_price:
                min_price = float(min_price)
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                max_price = float(max_price)
                queryset = queryset.filter(price__lte=max_price)
        except ValueError:
            pass  # Optionally handle invalid price values here

        if in_stock:
            queryset = queryset.filter(stock_quantity__gt=0 if in_stock.lower() == 'true' else 0)

        return queryset

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product = Product.objects.get(id=self.kwargs['product_id'])
        serializer.save(user=self.request.user, product=product)

class ProductReviewsListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_id'])
    
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductImageUploadView(APIView):
    def post(self, request, product_id):
        product = Product.objects.get(id=product_id)
        images = request.FILES.getlist('images')
        image_instances = [ProductImage(product=product, image=image) for image in images]
        ProductImage.objects.bulk_create(image_instances)
        serializer = ProductImageSerializer(image_instances, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)