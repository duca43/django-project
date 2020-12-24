from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from djangoproject.djangoapp.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me', UserViewSet.as_view({'get': 'get_current_user'}), name='current_user'),
    path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='user')
]
