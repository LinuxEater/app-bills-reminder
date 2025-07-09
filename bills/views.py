from django.shortcuts import render, redirect
from datetime import timedelta
from .models import Conta
from .forms import ContaForm
from datetime import date
from dateutil.relativedelta import relativedelta


# Create your views here.

def lista_contas(request):
    contas = Conta.objects.order_by('vencimento')
    context = {
        'contas': contas
    }
    return render(request, 'lista.html', context)


def gerar_contas_mensais():
    hoje = date.today()
    contas_recorrentes = Conta.objects.filter(recorrente=True)

    for conta in contas_recorrentes:
        # Evita criar mais de uma vez no mesmo mês
        if conta.vencimento < hoje and conta.ultima_geracao != hoje:
            nova_data = conta.vencimento + relativedelta(months=conta.intervalo_meses or 1)

            # Cria nova conta com mesmo valor e título
            nova_conta = Conta.objects.create(
                titulo=conta.titulo,
                valor=conta.valor,
                vencimento=nova_data,
                pago=False,
                recorrente=True,
                intervalo_meses=conta.intervalo_meses,
                ultima_geracao=hoje
            )

            # Atualiza a conta original
            conta.ultima_geracao = hoje
            conta.save()


def contas_a_vencer():
    hoje = date.today()
    return Conta.objects.filter(vencimento__lte=hoje + timedelta(days=3), pago=False)