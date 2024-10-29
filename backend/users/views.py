from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

# Register a new user
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all() # retrieve all User objects
    serializer_class = UserSerializer # Use User serializer for data conversion
    permission_classes = [AllowAny] # no authentication required for this view so anyone can register

# Retrieve user profile
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user