from django.forms import ModelForm
from Booking.models import ProductCat, ProductModel, BookingModel
# from django_select2 import forms as s2forms
from django import forms
from Booking.models import ProductModel


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

        def form_valid(self, form):
            services = form.cleaned_data.get('services')
            instance = BookingModel.objects.create(services=services)

            for i in services:
                instance.services.set(i)

            data = ProductModel.objects.all()

            for i in data:
                choices = [('i.id', 'i.name')]
            
            services = forms.ChoiceField(choices=choices, widget=Select2MultipleWidget)