from django.db import models

class Style(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brewery(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_country(self):
        return self.country


class Beer(models.Model):
    style = models.ForeignKey('Style', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    volume = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    abv = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brewery = models.ForeignKey('Brewery', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
