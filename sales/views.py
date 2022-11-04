from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template
from django.urls import reverse
from xhtml2pdf import pisa

from products.models import Produto
from sales.forms import VendasForm
from sales.models import Venda


def sales(request):
    sales_form_data = request.session.get('sales_form_data') or None
    form = VendasForm(sales_form_data)
    vendas = Venda.objects.all().order_by('-id')

    page_number = request.GET.get('page', 1)
    paginator = Paginator(vendas, 5)
    page_obj = paginator.get_page(page_number)

    context = {'form': form, 'vendas': page_obj}

    return render(request,  'sales/sales.html', context)


def create_sales(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['sales_form_data'] = POST
    form = VendasForm(POST)

    if form.is_valid():
        form_venda = form.save(commit=False)
        form_venda.vendedor = request.user

        form_venda.save()

        produto = Produto.objects.get(id=request.POST.get('produto'))
        produto.vendido = True
        produto.save()

        del(request.session['sales_form_data'])
        messages.success(request, 'Venda cadastrada')

    return redirect(reverse('sales:sales'))


def view_nota_fiscal(request, id_sale):
    sales_form_data = request.session.get('sales_form_data') or None
    form = VendasForm(sales_form_data)
    venda = Venda.objects.get(id=id_sale)
    context = {'form': form, 'venda': venda}

    return render(request, 'sales/view_nota_fiscal.html', context)


def down_nota_fiscal(request, id_sale):
    venda = Venda.objects.get(id=id_sale)

    template_path = 'sales/down_nota_fiscal.html'
    context = {'venda': venda}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="nota-fiscal-{venda.produto}.pdf"'  # noqa: E501
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
