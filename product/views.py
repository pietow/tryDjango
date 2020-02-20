from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, rawProductForm


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    print(request)
    context = {
        'object_list': queryset
    }
    return render(request, "product/product_list.html", context)


def product_detail_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object': obj
    }
    return render(request, "product/product_detail.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    context = {
        'object': obj
    }
    return render(request, "product/product_delete.html", context)


def dynamic_lookup_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {'object': obj}
    return render(request, "product/product_detail.html", context)
