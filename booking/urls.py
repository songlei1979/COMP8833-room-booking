
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from .views import register, login, profile, api_root

from .viewsets import BookingViewSet

router = DefaultRouter()
router.register('bookings', BookingViewSet, basename='booking')
router.APIRootView.permission_classes = [AllowAny]
urlpatterns = [
    path('', api_root, name='api-root'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('', include(router.urls)),
]
