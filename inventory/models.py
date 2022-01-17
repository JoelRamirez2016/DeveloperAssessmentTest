from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    gov_id = models.CharField(max_length=20)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    subtotal = models.IntegerField()
    taxes = models.IntegerField()
    paid = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Shippping(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    cost = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Payment(models.Model):
    class Types(models.IntegerChoices):
        CASH = 1
        CHECKS =  2
        DEBIT_CARDS = 3
        CREDIT_CARDS = 4
        MOBILE_PAYMENTS = 5
        ELECTRONIC_BANK_TRANSFER = 6

    class Taxes(models.IntegerChoices):
        NO_TAX = 0
        INDIVIDUAL_INCOME_TAXES = 1
        CORPORATE_INCOME_TAXES = 2
        PAYROLL_TAXES = 3
        CAPITAL_GAINS_TAXES = 4
        SALES_TAXES = 5
        GROSS_RECEIPTS_TAXES = 6
        VALUE_ADDED_TAXES = 7
        EXCISE_TAXES = 8

    type = models.CharField(
        max_length=2,
        choices=Taxes.choices,
        default=Taxes.NO_TAX,
    )
    tax = models.CharField(
        max_length=2,
        choices=Types.choices,
        default=Types.CASH,
    )
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    total = models.IntegerField()
