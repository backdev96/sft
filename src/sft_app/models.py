from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Manufacturer name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")


class Contract(models.Model):
    name = models.CharField(max_length=255, verbose_name="Cotract name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name="Application name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    contract = models.ForeignKey(
        Contract,
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="Contract"
    )


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product name")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Application"
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="manufacturers"
    )
