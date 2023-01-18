from django.forms import ModelForm
from Booking.models import ProductCat, ProductModel, BookingModel
from django import forms
from django_select2.forms import Select2MultipleWidget

from Booking.models import ProductModel
# from better_filter_widget import BetterFilterWidget


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
        services = forms.ModelMultipleChoiceField(queryset=ProductModel.objects.all(), widget=forms.SelectMultiple(attrs={'class':'select2'}))