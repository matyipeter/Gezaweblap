from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Reference(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="reference/", null=True, blank=True)

    def __str__(self):
        return self.name