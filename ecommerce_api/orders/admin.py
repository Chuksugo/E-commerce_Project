from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'status', 'created_date')
    list_filter = ('status',)
    search_fields = ('product__name', 'status')

    def save_model(self, request, obj, form, change):
        """
        Override save method to handle custom logic for stock reduction.
        This method ensures stock quantity is properly adjusted when the order is saved.
        """
        if not change:  # Only execute logic for new orders
            if obj.product.stock_quantity < obj.quantity:
                raise ValueError("Not enough stock available.")
            obj.product.stock_quantity -= obj.quantity
            obj.product.save()
        super().save_model(request, obj, form, change)
