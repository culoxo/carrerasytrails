from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from .models import calendario
from .filters import FiltroPrueba
# Create your views here.


def index(request):
    orders = calendario.objects.all()
    miFiltro=FiltroPrueba(request.GET, queryset=orders)
    orders = miFiltro.qs
    carreras= calendario.objects.order_by('fecha')[:5]
    context= {'miFiltro': miFiltro, 'carreras': carreras}
    return render(request, 'mainapp/index.html', context )


def blog(request):
    orders = calendario.objects.all()
    miFiltro=FiltroPrueba(request.GET, queryset=orders)
    orders = miFiltro.qs
    carreras= calendario.objects.order_by('fecha')[:5]
    context= {'miFiltro': miFiltro, 'carreras': carreras}
    
    return render (request, 'mainapp/blog.html',
        context)

def salida(request):
    orders = calendario.objects.all()
    miFiltro=FiltroPrueba(request.GET, queryset=orders)
    orders = miFiltro.qs
    carreras= calendario.objects.order_by('fecha')[:5]
    context= {'miFiltro': miFiltro, 'carreras': carreras}
    
    return render (request, 'mainapp/salida.html',
        context)

def montana(request):
    orders = calendario.objects.all()
    miFiltro=FiltroPrueba(request.GET, queryset=orders)
    orders = miFiltro.qs
    carreras= calendario.objects.order_by('fecha')[:5]
    context= {'miFiltro': miFiltro, 'carreras': carreras}
    return render (request, 'mainapp/montana.html', context)


def buscador(request):
    orders = calendario.objects.all()
    miFiltro=FiltroPrueba(request.GET, queryset=orders)
    orders = miFiltro.qs
    carreras= calendario.objects.order_by('fecha')[:5]
    context= {'miFiltro': miFiltro, 'carreras': carreras}
    return render(request, 'mainapp/buscador.html', context)



def elFiltro(request):
    orders = calendario.objects.order_by('fecha')
    miFiltro=FiltroPrueba(request.GET, queryset=orders)
    orders = miFiltro.qs 
    carreras= calendario.objects.order_by('fecha')[:5]
    context= {'miFiltro': miFiltro, 'carreras': carreras}
    return render(request, 'mainapp/prueba1.html', context )

