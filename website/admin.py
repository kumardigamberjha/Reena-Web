from django.contrib import admin

from website.models import ContactUsPage, CartItem, CartBookingModel, Timings

admin.site.register(Timings)
admin.site.register(ContactUsPage)
admin.site.register(CartItem)
admin.site.register(CartBookingModel)