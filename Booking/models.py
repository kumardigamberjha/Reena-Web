from django.db import models


class ProductCat(models.Model):
    name = models.CharField(max_length= 150)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    name = models.CharField(max_length= 150)
    price = models.IntegerField()
    cat = models.ForeignKey(ProductCat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BookingModel(models.Model):
    name = models.CharField(max_length=75)
    phone = models.CharField(max_length=10)
    services = models.ManyToManyField(ProductModel)
    datentime = models.DateTimeField()
    total_payment = models.CharField(max_length=20)
    payent_rec = models.IntegerField(blank=True, null=True)
    pending_paymnet = models.IntegerField(blank=True, null=True)
    BookingTime = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=30)

    def __str__(self):
        return self.name