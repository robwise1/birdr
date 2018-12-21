from django.test import TestCase

from profiles.forms import UserRegistrationForm


class UserRegistrationFormTestCase(TestCase):
    def test_form_fields(self):
        form_fields = {'username': 'bones',
                     'password1': 'abcdefggg',
                     'password2': 'abcdefggg',
                     'email': 'bananas@farm.com'}
        form = UserRegistrationForm(form_fields)
        self.assertTrue(form.is_valid())

    def test_password_too_short(self):
        form_fields = {'username': 'bones',
                     'password1': 'asdf',
                     'password2': 'asdf',
                     'email': 'bananas@farm.com'}
        form = UserRegistrationForm(form_fields)
        self.assertFalse(form.is_valid())