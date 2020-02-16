from django.shortcuts import render
from .models import Product
from .forms import ProductForm, rawProductForm
# Create your views here.
#def product_create_view(request):
#	my_form = rawProductForm()
#	if request.POST:
#		my_form = rawProductForm(request.POST)
#		if my_form.is_valid():
#			print(my_form.cleaned_data)
#			Product.objects.create(**my_form.cleaned_data)
#		else:
#			print(my_form.errors)
#	context = {
#		"form": my_form
#	}
#	return render(request, "product/product_create.html", context)
  
def product_create_view(request):
	initial_data = {
		"title": "awesome"
		}
	obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
	if form.is_valid():
		form.save()
	context = {
	    'form': form
	}
	return render(request, "product/product_create.html", context)

#def product_create_view(request):
#    form = ProductForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = ProductForm() #empties text fields after submission
#    context = {
#        'form': form
#    }
#    return render(request, "product/product_create.html", context)

def product_detail_view(request):
	obj = Product.objects.get(id=1)
   # context = {
   # 'title'      : obj.title,
   # 'description': obj.description
   # }
	context = {
		'object': obj
	}
	return render(request, "product/product_detail.html", context)
