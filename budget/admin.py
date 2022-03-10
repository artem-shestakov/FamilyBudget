from django.contrib import admin
from .models import Wallet, Incomes, Savings

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass

@admin.register(Incomes)
class IncomesAdmin(admin.ModelAdmin):
    pass


@admin.register(Savings)
class IncomesAdmin(admin.ModelAdmin):
    pass