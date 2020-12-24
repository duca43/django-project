from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions, response, status, views, viewsets, mixins

class CurrentUserView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):          
        response_serializer = UserSerializer(request.user)
        return response.Response(response_serializer.data, status.HTTP_200_OK)

class UserViewSet(viewsets.GenericViewSet,
                 mixins.RetrieveModelMixin):
                
    queryset = User
    serializer_class = UserSerializer
