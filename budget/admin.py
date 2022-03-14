from django.contrib import admin
from .models import Wallet, Source, Saving, Transaction

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass

@admin.register(Source)
class sourcesAdmin(admin.ModelAdmin):
    pass


@admin.register(Saving)
class SourcesAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass