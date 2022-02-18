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

    def __str__(self) -> str:
        return self.owner.email

class Incomes(models.Model):
    title = models.CharField(max_length=250, blank=False)
    created_at = models.DateField()
    is_active = models.BooleanField(default=True)

class Savings(models.Model):
    title = models.CharField(max_length=250, blank=False)
    amount = models.FloatField()
    created_at = models.DateField()
    is_active = models.BooleanField(default=True)

class Costs(models.Model):
    title = models.CharField(max_length=250, blank=False)
    amount = models.FloatField()
    limit = models.FloatField()
    created_ad = models.DateField()
    is_active = models.BooleanField(default=True)
