from django.urls import path
from .views import LoginUserView, RegisterUserView, UserProfileView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile')
]
