from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import ContactUsPage
from Pages.models import Homepage, AboutUsPage, DermaLogicaPage, IPLPage, CaciSynergyPage, MakeUpPage, ManPage, MassagePage, EarPage, GiftPage, NailPage, WaxingPage, ElectroPage, TintingPage


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


class CaciForm(ModelForm):
    class Meta:
        model = CaciSynergyPage
        fields = "__all__"


class WaxingForm(ModelForm):
    class Meta:
        model = WaxingPage
        fields = "__all__"


class NailForm(ModelForm):
    class Meta:
        model = NailPage
        fields = "__all__"


class MakeUpForm(ModelForm):
    class Meta:
        model = MakeUpPage
        fields = "__all__"



class TintingForm(ModelForm):
    class Meta:
        model = TintingPage
        fields = "__all__"


class EarPForm(ModelForm):
    class Meta:
        model = EarPage
        fields = "__all__"


class ElectroForm(ModelForm):
    class Meta:
        model = ElectroPage
        fields = "__all__"


class ManForm(ModelForm):
    class Meta:
        model = ManPage
        fields = "__all__"


class MassageForm(ModelForm):
    class Meta:
        model = MassagePage
        fields = "__all__"