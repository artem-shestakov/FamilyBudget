from pyexpat import model
from turtle import title
from django.utils import timezone
from django.db import models

from users.models import Family, User


class Wallet(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True,
        related_name='wallet'
    )
    family = models.OneToOneField(
        Family,
        on_delete=models.PROTECT,
        related_name='wallet',
        blank=True,
        null=True
    )
    balance = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    expenses = models.FloatField(
        default=0,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return self.owner.email

class Bucket(models.Model):
    wallet = models.ForeignKey(
        Wallet,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    title = models.CharField(
        unique=True,
        max_length=250,
        blank=False
    )
    created_at = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    amount = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.wallet)+'-'+str(self.title)

class Source(Bucket):
    plan = models.FloatField(default=0)

class Saving(Bucket):
    pass

class Expense(Bucket):
    limit = models.FloatField()

class Transaction(models.Model):
    date = models.DateTimeField(
        default=timezone.now,
        null=False,
        blank=False
    )
    source = models.ForeignKey(
        Bucket,
        related_name='source_transaction',
        on_delete=models.PROTECT
    )
    target = models.ForeignKey(
        Bucket,
        related_name='target',
        on_delete=models.PROTECT
    )
    amount = models.FloatField(
        blank=False,
        null=False
    )
    comment = models.TextField(
        blank=True
    )
