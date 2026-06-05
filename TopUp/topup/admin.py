from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('game', 'nominal', 'payment', 'total', 'created_at')
    list_filter = ('payment', 'created_at')