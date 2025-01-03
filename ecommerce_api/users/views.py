from rest_framework import generics, permissions, filters
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

# Custom Permission Class to allow Admin to access all users and regular users to access only their own profile
class IsAdminOrSelf(permissions.BasePermission):
    """
    Custom permission to allow admins to view and edit any user,
    and users to view or edit their own profile.
    """
    def has_object_permission(self, request, view, obj):
        # Admins can view and edit any user
        if request.user.is_staff:
            return True
        # Regular users can only view or edit their own profile
        return obj == request.user

# View to list all users and create a new user (Admins only)
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email']

    def perform_create(self, serializer):
        # Only admin users can create new users
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to create users.")

# View to retrieve, update, or delete a specific user's profile
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelf]
