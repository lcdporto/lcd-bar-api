from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Payment(models.Model):
    barcode = models.IntegerField()
    pin = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
