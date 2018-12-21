from django import forms
from django_registration.forms import RegistrationFormCaseInsensitive

from profiles.models import User 
class UserRegistrationForm(RegistrationFormCaseInsensitive):
    """ Form to register new users """
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')