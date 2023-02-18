from django.db import models


class ContactUsPage(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class CartBookingModel(models.Model):
    name = models.CharField(max_length=75)
    phone = models.CharField(max_length=15, blank=True, null=True)
    datentime = models.DateTimeField()
    total_payment = models.CharField(max_length=20)
    services = models.ManyToManyField(CartItem)
    username = models.CharField(max_length=35)
    BookingTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
