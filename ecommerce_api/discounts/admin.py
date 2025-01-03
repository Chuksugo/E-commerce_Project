from django.contrib import admin
from .models import Discount
from products.models import Product  # Correct import for Product model

admin.site.register(Discount)
