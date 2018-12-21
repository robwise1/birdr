from django.contrib.auth.views import LoginView, LogoutView
from django_registration.backends.one_step.views import RegistrationView

from tools.decorators import anonymous_required
from profiles.forms import UserRegistrationForm

@anonymous_required
def register(request, *args, **kwargs):
    view = RegistrationView.as_view(form_class=UserRegistrationForm)
    return view(request, *args, **kwargs)

@anonymous_required
def login(request, *args, **kwargs):
    view = LoginView.as_view()
    return view(request, *args, **kwargs)

def logout(request, *args, **kwargs):
    view = LogoutView.as_view()
    return view(request, *args, **kwargs)