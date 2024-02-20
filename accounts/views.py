from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import CustomPasswordResetSerializer, RegisterSerializer
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from rest_framework import (
    permissions,
    response,
    status,
)
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate and include authentication token in the response
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'user': MyTokenObtainPairSerializer(user.first_name).data,
            'access_token': access_token,
        }, status=status.HTTP_201_CREATED)
    

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