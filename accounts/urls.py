from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from .views import MyObtainTokenPairView, UserDetailAPIView, CustomPasswordResetConfirmView, \
                CustomPasswordResetView, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('password/reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('profile/<pk>/', UserDetailAPIView.as_view(), name='detail'),
]
