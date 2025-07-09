from django.contrib import admin
from .models import Conta
from django.contrib import admin

admin.site.site_header = "App Bill Reminder Admin"

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor', 'vencimento', 'pago')  # removido 'criado_em'
    list_filter = ('pago', 'vencimento')
    search_fields = ('titulo', 'descricao')