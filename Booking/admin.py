from django.contrib import admin

from Booking.models import ProductCat, ProductModel, BookingModel

admin.site.register(ProductModel)
admin.site.register(ProductCat)
admin.site.register(BookingModel)