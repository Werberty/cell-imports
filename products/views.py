from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProdutoForm
from .models import Produto


@login_required(login_url='/auth/login')
def home(request):
    return render(request, 'products/home.html')


@login_required(login_url='/auth/login')
def products(request):
    product_form_data = request.session.get('product_form_data') or None
    produtos = Produto.objects.filter(vendido=False).order_by('-id')
    form = ProdutoForm(product_form_data)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(produtos, 5)
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/products.html', context={
        'produtos': page_obj,
        'form': form,
    })


@login_required(login_url='/auth/login')
def create_product(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['product_form_data'] = POST
    form = ProdutoForm(POST)

    if form.is_valid():
        form_prod = form.save(commit=False)
        form_prod.vendedor = request.user
        codigo = form_prod.codigo_produto
        exists = Produto.objects.filter(
            codigo_produto=codigo).exists()

        if exists:
            messages.error(request, 'Código do produto já existe')
            return redirect(reverse('products:products'))

        form_prod.save()
        del(request.session['product_form_data'])
        messages.success(request, 'Produto cadastrado')

    return redirect(reverse('products:products'))


@login_required(login_url='/auth/login')
def delete_product(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    product_id = POST.get('id')

    product = Produto.objects.get(
        id=product_id,
        vendido=False
    )

    if not product:
        raise Http404()

    product.delete()
    messages.add_message(request, constants.WARNING, 'Produto deletado')
    return redirect(reverse('products:products'))


@login_required(login_url='/auth/login')
def edit_product(request, product_id):
    produto = get_object_or_404(Produto, id=product_id, vendido=False)
    produtos = Produto.objects.filter(vendido=False).order_by('-id')
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
            form_prod = form.save(commit=False)

            codigo = form_prod.codigo_produto
            exists = Produto.objects.filter(
                codigo_produto=codigo
            ).exclude(id=produto.id).exists()

            if exists:
                messages.error(request, 'Código do produto já existe')
                return render(request, 'products/edit_product.html', context={
                    'form': form,
                    'produto': produto,
                    'produtos': produtos,
                })

            form_prod.save()

            messages.add_message(request, constants.SUCCESS, 'Produto editado')
            return redirect(reverse('products:products'))
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao editar')
            return render(request, 'products/edit_product.html', context={
                'form': form,
                'produto': produto,
                'produtos': produtos,
            })


@login_required(login_url='/auth/login')
def detail_product(request, product_id):
    produto = get_object_or_404(Produto, id=product_id)

    return render(request, 'products/detail_product.html', context={
        'produto': produto,
    })
