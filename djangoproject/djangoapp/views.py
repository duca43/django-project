from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

@api_view()
@permission_classes((IsAuthenticated,))
def user(request):
    serializer = UserSerializer(context={'request': request}, instance=request.user)
    return Response({"message": "Your data is retrieved successfully!", "data": serializer.data})
