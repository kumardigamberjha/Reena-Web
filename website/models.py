from django.db import models

class Homepage(models.Model):
    home1 = models.TextField()
    home2 = models.TextField()
    home3 = models.TextField()
    home4 = models.TextField()
    home5 = models.TextField()

    def __str__(self):
        return self.home1

class ContactUsPage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        