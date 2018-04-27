from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from shop.models import Aorder

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name  = forms.CharField(max_length=100, required=True)
    email      = forms.EmailField(max_length=254, help_text='eg. youremail@anyemail.com')
    

    class Meta:
        model =User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        es = User.objects.filter(email= email)
        if es.exists():
            raise forms.ValidationError("Email is taken.")
        return email

class AorderForm(ModelForm):
    class Meta:
        model = Aorder
        fields = ['ups', 'desx', 'desy']


