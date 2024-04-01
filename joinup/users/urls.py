from django.urls import path
from .views import UserRegisterView, UserProfileView

urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
