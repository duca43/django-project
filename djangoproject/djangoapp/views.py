from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions, response, status, views, viewsets, mixins
from rest_framework.decorators import action

class UserViewSet(viewsets.GenericViewSet,
                 mixins.RetrieveModelMixin):
                
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, url_path='me', permission_classes=[permissions.IsAuthenticated])
    def get_current_user(self, request):          
        response_serializer = UserSerializer(request.user)
        return response.Response(response_serializer.data, status.HTTP_200_OK)
