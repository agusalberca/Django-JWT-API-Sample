from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Wallet(models.Model):
    dir = models.CharField(max_length=64, verbose_name='dir', primary_key=True)
    balance = models.FloatField(default=0)
    #TODO Validate dir data when creating instance

class Transaction(models.Model):
    amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now)
    from_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name='from_transactions')
    to_wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name='to_transactions')
    #TODO implement linear regression model based on transaction execution