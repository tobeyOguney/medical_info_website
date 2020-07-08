from django import forms    
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_practitioner']
        labels = {
            'username': "Username",
            'first_name': "First Name",
            'last_name': "Last Name",
            'email': "Email Address",
            'is_practitioner': "Medical Practitioner?"
        }
    
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['is_practitioner'].required = True
