from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import CustomPasswordResetSerializer
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from rest_framework import (
    permissions,
    response,
    status,
)
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser, UserProfile
from .serializers import RegisterSerializer
from rest_framework.response import Response


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = CustomUser()
        for key, value in serializer.validated_data.items():
            setattr(user, key, value)
        user.set_password(serializer.validated_data['password'])
        user.save()
        UserProfile.objects.create(user=user)

class UserDetailAPIView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = MyTokenObtainPairSerializer
    permission_class = [permissions.IsAuthenticated]
    
    def get_object(self):
        user_id = self.request.user.id
        return CustomUser.objects.filter(id=self.kwargs['pk']).prefetch_related('profile').first()
    

class CustomPasswordResetView(PasswordResetView):
    serializer_class = CustomPasswordResetSerializer

    def post(self, request, *args, **kwargs):
        # Add any additional custom logic here if needed
        return super().post(request, *args, **kwargs)
    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    # You can customize the view if needed
    def post(self, request, *args, **kwargs):
        # Add any additional custom logic here if needed
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            # You can add additional data to the response if needed
            response.data['custom_key'] = 'custom_value'
        return response