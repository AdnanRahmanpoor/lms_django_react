from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

# Register a new user
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all() # retrieve all User objects
    serializer_class = UserSerializer # Use User serializer for data conversion
    permission_classes = [AllowAny] # no authentication required for this view so anyone can register

# Login 
class LoginUserView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)

# Retrieve user profile
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    

# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework.permissions import AllowAny

# class LoginUserView(APIView):
#     permission_classes = [AllowAny]  # Allow access to unauthenticated users
    
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
