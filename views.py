from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
from .models import Transacao
from .forms import TransacaoForm

def home(request):

    data = {}
    
    #data['lista'] = [1,2,3,4,5,6,7,8,9]
    #data['now'] = datetime.datetime.now()
       
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}

    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)

def criar(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return listagem(request)
    
    form = TransacaoForm()
    return render(request, 'contas/form.html', {'form': form})

def update(request, pk):
    data = {}

    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    
    if form.is_valid():
        form.save()
        return redirect(listagem)
    
    data['form'] = form
    data['transacao'] = transacao 
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()

    return redirect(listagem)