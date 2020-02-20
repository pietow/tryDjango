from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from product.models import Product


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, my_id, *args, **kwargs):
    obj = get_object_or_404(Product, id=my_id)
    my_context = {
        "title"    : "this about us",
        "my_number": 123,
        "my_list"  : [123, 456, 789],
        "my_html"  : "<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")
