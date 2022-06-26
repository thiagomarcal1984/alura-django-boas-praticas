from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from receitas.models import Receita

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    dados = {
        'receitas' : receitas
    }
    return render(request, 'receitas/index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request, 'receitas/receita.html', receita_a_exibir)

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')

def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita' : receita}
    return render(request, 'receitas/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    receita_id = request.POST['receita_id']
    r = Receita.objects.get(pk=receita_id)
    if request.method == 'POST':
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.user = get_object_or_404(User, pk=request.user.id)
        r.save()
        return redirect('dashboard')
    else:
        return redirect('edita_receita', receita_id=receita_id)

