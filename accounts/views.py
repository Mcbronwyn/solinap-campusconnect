from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, ProfileUpdateForm

User = get_user_model()

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account created successfully! You can now log in."

class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = "registration/profile.html"
    success_url = reverse_lazy("profile")
    success_message = "Your profile has been updated successfully."

    def get_object(self, queryset=None):
        # Strict security: forces UpdateView to only return the currently authenticated user
        return self.request.user