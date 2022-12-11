from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente

@login_required(login_url='/auth/')
def Clientes(request):
    username = request.user
    clientes_cadastrados = Cliente.objects.all()
    
    context = {
        'username': username,
        'clientes_cadastrados': clientes_cadastrados,
    }
    return render(request, 'cadastro_clientes/clientes.html', context)

@login_required(login_url='/auth/')
def NovoCliente(request):
    if request.method == 'POST':
        nome_cliente = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']

        if nome_cliente.strip() != '' or sobrenome.strip() != '' or telefone.strip() != '':
            novo_cliente = Cliente(nome=nome_cliente, sobrenome=sobrenome, telefone=telefone, endereco=endereco)
            novo_cliente.save()
            return redirect('/clientes/novo_cliente/')
        

    username = request.user
    
    context = {
        'username': username,
    }
    return render(request, 'cadastro_clientes/novo_cliente.html', context)