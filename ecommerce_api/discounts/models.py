from django.db import models
from products.models import Product  # Import Product model
from django.utils import timezone  # Import timezone

class Discount(models.Model):
    product = models.ForeignKey(Product, related_name='discounts', on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Discount percentage
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.percentage}% off for {self.product.name}"

    def is_active(self):
        # Check if the discount is within the valid date range
        now = timezone.now()  # Get the current time
        return self.active and self.start_date <= now <= self.end_date  # Check if the discount is active

