from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProdutoForm
from .models import Produto


@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'products/home.html')


@login_required(login_url='/auth/login')
def products(request):
    if request.method == 'GET':
        produtos = Produto.objects.filter(
            vendedor=request.user).order_by('-id')
        form = ProdutoForm()
        return render(request, 'products/products.html', context={
            'produtos': produtos,
            'form': form,
        })

    elif request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form_prod = form.save(commit=False)
            form_prod.vendedor = request.user
            form_prod.save()
            messages.add_message(
                request, constants.SUCCESS, 'Produto cadastrado')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar')

        produtos = Produto.objects.filter(
            vendedor=request.user).order_by('-id')
        form = ProdutoForm()

        return render(request, 'products/products.html', context={
            'produtos': produtos,
            'form': form,
        })


@login_required(login_url='/auth/login')
def delete_product(request, product_id):
    product = Produto.objects.filter(id=product_id)

    if request.method == 'GET':
        return redirect('/products')

    if request.method == 'POST':
        product.delete()
        messages.add_message(request, constants.WARNING, 'Produto deletado')
        return redirect('/products')


@login_required(login_url='/auth/login')
def edit_product(request, product_id):
    produto = get_object_or_404(Produto, id=product_id)
    produtos = Produto.objects.filter(
        vendedor=request.user).order_by('-id')
    form = ProdutoForm(instance=produto)
    if request.method == 'GET':
        return render(request, 'products/edit_product.html', context={
            'form': form,
            'produto': produto,
            'produtos': produtos,
        })
    elif request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Produto editado')
            return redirect('/products')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao editar')
            return render(request, 'products/edit_product.html', context={
                'form': form,
                'produto': produto,
                'produtos': produtos,
            })
