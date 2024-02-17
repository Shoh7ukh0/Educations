from .serializers import UserSerializer, UserProfileSerializer, CustomPasswordResetSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token')
        user_id = response.data.get('user_id')
        return Response({'token': token, 'user_id': user_id})
    

class SignUpView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})
    
    
class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

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