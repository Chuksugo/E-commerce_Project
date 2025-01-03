from django.db import models, transaction
from django.core.exceptions import ValidationError
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('purchased', 'Purchased'),
        ('canceled', 'Canceled'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reserved')
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Custom save method to manage stock reduction when a new order is created.
        It ensures stock is sufficient before reducing it.
        """
        if not self.pk:  # Only run logic for new orders
            if self.product.stock_quantity < self.quantity:
                raise ValidationError("Not enough stock available.")
            
            # Use a transaction to prevent inconsistencies in case of errors
            with transaction.atomic():
                self.product.stock_quantity -= self.quantity
                self.product.save()

        super().save(*args, **kwargs)

    def cancel_order(self):
        """
        Custom method to cancel an order and revert stock for reserved orders.
        """
        if self.status == 'reserved':
            with transaction.atomic():
                self.product.stock_quantity += self.quantity
                self.product.save()
                self.status = 'canceled'
                self.save()
        else:
            raise ValidationError("Only reserved orders can be canceled.")

    def __str__(self):
        return f"Order {self.id} - {self.product.name} ({self.status})"
