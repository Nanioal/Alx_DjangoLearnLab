# accounts/views.py

from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer

CustomUser = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    permission_classes = [permissions.IsAuthenticated]  # Corrected to permissions.IsAuthenticated

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Corrected to permissions.IsAuthenticated

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return JsonResponse({"message": "User followed"})

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated] 

