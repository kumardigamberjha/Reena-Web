from django.forms import ModelForm
from Booking.models import ProductCat, ProductModel, BookingModel
from django import forms
from Booking.models import ProductModel
from django_select2 import forms as s2forms

class ProductWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "services__icontains",
    ]

class ProductCatForm(ModelForm):
    class Meta:
        model = ProductCat
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"


class BookingModelForm(ModelForm):
    class Meta:
        model = BookingModel
        fields = "__all__"
