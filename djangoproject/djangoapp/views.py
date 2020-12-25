from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import response, status, views, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

class UserViewSet(viewsets.GenericViewSet,
                 mixins.RetrieveModelMixin):
                
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        user = super().retrieve(request, pk).data
        user_to_return = {
            'first_name': user['first_name'],
            'last_name': user['last_name']
        }
        return response.Response({'user': user_to_return}, template_name='user.html') 
        
    @action(detail=False, url_path='me', permission_classes=[IsAuthenticated], renderer_classes=[JSONRenderer]) 
    def get_current_user(self, request):          
        response_serializer = UserSerializer(request.user)
        return response.Response(response_serializer.data, status.HTTP_200_OK)

class HomeView(views.APIView):
    
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):
        return response.Response(template_name='home.html')

class TestView(views.APIView):

    def get(self, request):
        return response.Response(status=status.HTTP_200_OK)

    def post(self, request):
        return response.Response(status=status.HTTP_201_CREATED)

    def put(self, request):
        return response.Response(status=status.HTTP_200_OK)

    def patch(self, request):
        return response.Response(status=status.HTTP_200_OK)

    def delete(self, request):
        return response.Response(status=status.HTTP_204_NO_CONTENT)
