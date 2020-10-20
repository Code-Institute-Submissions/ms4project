import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Beer


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_quantity = models.DecimalField(max_digits=6, decimal_places=0,
                                         null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        ''' generate a random order number(UUID) '''

        return uuid.uuid4().hex.upper()

    def update_total(self, *args, **kwargs):
        """ update grand total each time line item is added,
            accounting for delivery costs. """
        self.total_quantity = self.lineitem.aggregate(Sum(
                            'quantity'))['quantity__sum']\
            or 0
        self.order_total = self.lineitem.aggregate(Sum(
                            'lineitem_total'))['lineitem_total__sum'] or 0
        if self.total_quantity < 6:
            self.delivery_cost = self.order_total *\
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override the default save method to set the order number
        if it hasn't been set already. """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitem')
    beer = models.ForeignKey(Beer, null=True, blank=False,
                             on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False)

    def save(self, *args, **kwargs):
        """ Override the default save method to set the order number
        if it hasn't been set already. """

        self.lineitem_total = self.beer.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.beer.sku} on order {self.order.order_number}'
