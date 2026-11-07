from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileUpdateView, SignUpView
from .forms import CustomAuthenticationForm

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(
        template_name="registration/login.html",
        authentication_form=CustomAuthenticationForm
    ), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]