from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import ContactUsPage


class CreateUserForm(UserCreationForm):
    # phone_no = forms.CharField(max_length = 10)
    class Meta:
        model = User
        fields = ["username","email","password1", 'password2']


class ContactForm(ModelForm):
    class Meta:
        model = ContactUsPage
        fields = "__all__"