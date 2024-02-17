from django.urls import path
from .views import SignUpView, LoginView, UserProfileView, CustomPasswordResetConfirmView, \
                CustomPasswordResetView

app_name = 'accounts'

urlpatterns = [
    path('password/reset/confirm/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
