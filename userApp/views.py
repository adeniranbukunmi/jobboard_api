
from rest_framework.decorators import api_view, permission_classes
from .serializer import CustomUserSerializer
from .models import CustomUserAcct
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(["POST"])
def registerUser(request):
    serialiser =CustomUserSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response({"message": "user created successfully", "data": serialiser.data}, status=status.HTTP_201_CREATED)
    return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
        
       

@api_view(["POST"])
def login(request):
    email=request.data.get("email")
    password=request.data.get("password")
    login_user=authenticate(email=email, password=password)
    if login_user:
        refresh = RefreshToken.for_user(login_user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)
