from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This about us",
        "my_number": 123,
        "my_list": [123, 456, 789]
    }
    return render(request, "about.html", my_context)


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")
