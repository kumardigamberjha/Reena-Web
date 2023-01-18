from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import ContactUsPage
from Pages.models import Homepage, AboutUsPage, DermaLogicaPage, IPLPage


class CreateUserForm(UserCreationForm):
    # phone_no = forms.CharField(max_length = 10)
    class Meta:
        model = User
        fields = ["username","email","password1", 'password2']


class ContactForm(ModelForm):
    class Meta:
        model = ContactUsPage
        fields = "__all__"
        

class HomeForm(ModelForm):
    class Meta:
        model = Homepage
        fields = "__all__"


class AboutUsForm(ModelForm):
    class Meta:
        model = AboutUsPage
        fields = "__all__"


class DermaForm(ModelForm):
    class Meta:
        model = DermaLogicaPage
        fields = "__all__"


class IPLForm(ModelForm):
    class Meta:
        model = IPLPage
        fields = "__all__"