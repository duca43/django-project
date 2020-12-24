from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from djangoproject.djangoapp.views import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)

print(router.get_urls())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls