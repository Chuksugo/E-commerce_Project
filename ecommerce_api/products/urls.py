from django.urls import path
from . import views
from .views import ProductImageUploadView

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', views.ProductRetrieveUpdateDeleteView.as_view(), name='product-detail'),
    path('products/<int:product_id>/reviews/', views.ProductReviewsListView.as_view(), name='product-reviews-list'),
    path('products/<int:product_id>/reviews/create/', views.ReviewCreateView.as_view(), name='create-review'),
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('products/<int:product_id>/upload-images/', ProductImageUploadView.as_view(), name='upload-product-images'),
]
