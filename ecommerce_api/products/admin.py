# products/admin.py
from django.contrib import admin
from .models import Category, Product, Review, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',)  
    list_filter = ('name',)  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category_name', 'stock_quantity', 'created_date', 'availability')
    search_fields = ('name', 'category__name')  
    list_filter = ('category', 'stock_quantity')  
    ordering = ('-created_date',)

    def category_name(self, obj):
        return obj.category.name if obj.category else 'No Category'
    category_name.admin_order_field = 'category'  
    category_name.short_description = 'Category'  

    def availability(self, obj):
        return 'In Stock' if obj.stock_quantity > 0 else 'Out of Stock'
    availability.short_description = 'Stock Availability'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__username', 'review_text')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'product']  
    search_fields = ['product__name']  
