from django.contrib import admin
from .models import Wallet, Sources, Savings

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass

@admin.register(Sources)
class sourcesAdmin(admin.ModelAdmin):
    pass


@admin.register(Savings)
class SourcesAdmin(admin.ModelAdmin):
    pass