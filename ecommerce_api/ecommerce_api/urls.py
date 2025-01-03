from django.contrib import admin
from django.urls import path, include
from .views import api_root
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', api_root, name='api-root'),
    path('api/products/', include('products.urls')),
    path('api/users/', include('users.urls')),
    path('api/wishlist/', include('wishlist.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/discounts/', include('discounts.urls')),
    path('', RedirectView.as_view(url='/api/', permanent=False)),  # Redirect root to /api/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
