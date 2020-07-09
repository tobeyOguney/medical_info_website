from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
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


class AgeForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('age',)


class SexForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('sex',)


class BloodTypeForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('blood_type',)


class GenotypeForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('genotype',)


class AIDSForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('AIDS_status',)


class MalariaForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('malaria_status',)


class EbolaForm(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('ebola_status',)


class COVID19Form(ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('COVID19_status',)
