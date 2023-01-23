from django.db import models
from ckeditor.fields import RichTextField 

class Homepage(models.Model):
    name=models.CharField(max_length=30)
    home1 = models.TextField()
    home2 = models.TextField()
    home3 = models.TextField()
    home4 = models.TextField()

    def __str__(self):
        return self.name


class AboutUsPage(models.Model):
    name=models.CharField(max_length=30)
    about1 = models.TextField()
    about2 = models.TextField()
    about3 = models.TextField()
    about4 = models.TextField()
    about5 = models.TextField()
    about6 = models.TextField()

    def __str__(self):
        return self.name


class DermaLogicaPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)
    dermahead3 = models.CharField(max_length=100)
    dermahead4 = models.CharField(max_length=100)
    dermahead5 = models.CharField(max_length=100)
    dermahead6 = models.CharField(max_length=100)
    dermahead7 = models.CharField(max_length=100)
    # dermahead8 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = models.TextField()
    derma3 = models.TextField()
    derma4 = models.TextField()
    derma5 = models.TextField()
    derma6 = models.TextField()
    derma7 = models.TextField()
    derma8 = models.TextField()

    def __str__(self):
        return self.name


class CaciSynergyPage(models.Model):
    name = models.CharField(max_length=30)
    cacihead1 = models.CharField(max_length=100)
    cacihead2 = models.CharField(max_length=100)
    cacihead3 = models.CharField(max_length=100)
    cacihead4 = models.CharField(max_length=100)
    cacihead5 = models.CharField(max_length=100)
    cacihead6 = models.CharField(max_length=100)
    cacihead7 = models.CharField(max_length=100)
    cacihead8 = models.CharField(max_length=100)
    cacihead9 = models.CharField(max_length=100)
    cacihead10 = models.CharField(max_length=100)
    cacihead11 = models.CharField(max_length=100)
    cacihead12 = models.CharField(max_length=100)

    caci1 = models.TextField()
    caci2 = models.TextField()
    caci3 = models.TextField()
    caci4 = models.TextField()
    caci5 = models.TextField()
    caci6 = models.TextField()
    caci7 = models.TextField()
    caci8 = models.TextField()
    caci9 = models.TextField()
    caci10 = models.TextField()
    caci11 = models.TextField()
    caci12 = models.TextField()

    def __str__(self):
        return self.name


class IPLPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = RichTextField()
    derma3 = RichTextField()
    
    def __str__(self):
        return self.name


class WaxingPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = models.TextField()
    
    def __str__(self):
        return self.name


class NailPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)
    dermahead3 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = RichTextField()
    derma3 = RichTextField()
    derma4 = models.TextField()

    def __str__(self):
        return self.name


class MakeUpPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = RichTextField()
    derma3 = RichTextField()
    derma4 = models.TextField()
    derma5 = RichTextField()


    def __str__(self):
        return self.name


class TintingPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)
    dermahead3 = models.CharField(max_length=100)
    dermahead4 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = models.TextField()
    derma3 = models.TextField()
    derma4 = models.TextField()
    derma5 = models.TextField()

    def __str__(self):
        return self.name


class EarPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = RichTextField()

    def __str__(self):
        return self.name


class ElectroPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)

    derma1 = RichTextField()
    derma2 = RichTextField()

    def __str__(self):
        return self.name


class ManPage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)
    dermahead3 = models.CharField(max_length=100)
    dermahead4 = models.CharField(max_length=100)
    dermahead5 = models.CharField(max_length=100)
    dermahead6 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = models.TextField()
    derma3 = models.TextField()
    derma4 = models.TextField()
    derma5 = models.TextField()
    derma6 = models.TextField()

    def __str__(self):
        return self.name


class MassagePage(models.Model):
    name = models.CharField(max_length=30)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)
    dermahead3 = models.CharField(max_length=100)
    dermahead4 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = models.TextField()
    derma3 = models.TextField()
    derma4 = models.TextField()
    derma5 = models.TextField()

    def __str__(self):
        return self.name


class GiftPage(models.Model):
    name = models.CharField(max_length=50)
    dermahead1 = models.CharField(max_length=100)
    dermahead2 = models.CharField(max_length=100)
    dermahead3 = models.CharField(max_length=100)
    dermahead4 = models.CharField(max_length=100)
    dermahead5 = models.CharField(max_length=100)
    dermahead6 = models.CharField(max_length=100)
    dermahead7 = models.CharField(max_length=100)

    derma1 = models.TextField()
    derma2 = models.TextField()
    derma3 = models.TextField()
    derma4 = models.TextField()
    derma5 = models.TextField()
    derma6 = models.TextField()
    derma7 = models.TextField()

    def __str__(self):
        return self.name