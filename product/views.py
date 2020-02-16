from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, rawProductForm
# Create your views here.


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
#	try:
#		obj = Product.objects.get(id=my_id)
#	except Product.DoesNotExist:
#		raise Http404
	context = {'object': obj}
	return render(request, "product/product_detail.html", context)
