from django.db import models

class Homepage(models.Model):
    name=models.CharField(max_length=30)
    home1 = models.TextField()
    home2 = models.TextField()
    home3 = models.TextField()
    home4 = models.TextField()

    def __str__(self):
        return self.name

class ContactUsPage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

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


class ContactUsPage(models.Model):
    name = models.CharField(max_length=30)
    about1 = models.TextField()
    about2 = models.TextField()
    about3 = models.TextField()
    about4 = models.TextField()
    about5 = models.TextField()
    about6 = models.TextField()

    def __str__(self):
        return self.name