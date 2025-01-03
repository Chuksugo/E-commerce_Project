# ecommerce_api/views.py
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "products": "/api/products/",
        "users": "/api/users/",
        "wishlist": "/api/wishlist/",
        "orders": "/api/orders/",
        "discounts": "/api/discounts/",
        "auth-token": "/api-token-auth/"
    })
