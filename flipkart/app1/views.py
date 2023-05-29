from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Products, Cars
from django.views.generic import ListView

# Create your views here.


def hello(request):
    return HttpResponse("Hello, world")


def index(request):
    return render(request, "sample.html")


def test(request):
    return render(request, "test.html")


def products(request):
    pdts = Products.objects.all().values()
    template = loader.get_template('prod.html')

    context = {
        'products': pdts,
    }
    return HttpResponse(template.render(context, request))


class CarsListView(ListView):
    model = Cars
    template_name = 'cars.html'
    context_object_name = 'cars'
