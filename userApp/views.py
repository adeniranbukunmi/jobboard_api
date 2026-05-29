from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializer import CustomUserSerializer
from .models import CustomUserAcct
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(["POST", "GET"])
def creatListUser(request):
    if request.method == "GET":
        users_info = CustomUserAcct.objects.all()
        serialiser = CustomUserSerializer(users_info, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serialiser =CustomUserSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response("user created successfully", serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, "something went wrong", status=status.HTTP_400_BAD_REQUEST)
        
       
@csrf_exempt
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
