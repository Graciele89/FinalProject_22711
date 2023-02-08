from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# using reverse_lazy to redirect the user to the login page upon successful registration
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
