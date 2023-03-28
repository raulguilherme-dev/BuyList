from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from List.models import *

# Create your views here.
def index(request):
    products = Product.objects.all
    lists = List.objects.all
    categories = Category.objects.all
    productsList = ProductsList.objects.all
    context = {
        'prods': products,
        'lists': lists,
        'categories': categories,
        'productsLists': productsList
    }
    return render(request, 'index.html', context)

def add_product(request):
    # inserir no meu banco de dados
    if request.method == 'POST':
        try:
            name = request.POST['name']
            description = request.POST['description']
            category = Category.objects.get(id = request.POST['category'])
            data = Product(
                name = name,
                description = description,
                category = category
            )
            data.save()
            return HttpResponseRedirect('/')

        except Exception as e:
            return HttpResponse("Ocorreu um erro ao salvar os dados")

def delete_product(request, pk):
    #if request.method == 'POST':
    prod = Product.objects.get(id = pk)
    prod.delete()
    return HttpResponseRedirect('/') 


def edit_product(request):
    if request.method == 'POST':
        prod = Product.objects.get(id = request.POST['id'])
        prod.name = request.POST['name']
        prod.description = request.POST['description']
        category = Category.objects.get(id = request.POST['category'])
        prod.category = category
        prod.save()
    return HttpResponseRedirect('/') 

def add_list(request):
    # inserir no meu banco de dados
    if request.method == 'POST':
        name = request.POST['name']
        data = List(
            name = name,
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_list(request, pk):
    #if request.method == 'POST':
    list = List.objects.get(id = pk)
    list.delete()
    return HttpResponseRedirect('/') 


def edit_list(request):
    if request.method == 'POST':
        list = List.objects.get(id = request.POST['id'])
        list.name = request.POST['name']
        list.save()
    return HttpResponseRedirect('/')

def add_product_to_list(request):
    if request.method == 'POST':
        lis = List.objects.get(id = request.POST['list'])
        prod = Product.objects.get(id = request.POST['product'])
        data = ProductsList(
            product = prod,
            list = lis
        )
        data.save()
    return HttpResponseRedirect('/')

def delete_product_from_list(li, pi):
    # if request.method == 'POST':
    # list_id = request.POST.get('list_id')
    # product_id = request.POST.get('product_id')
    print(li)
    lis = List.objects.get(id = li)
    prod = Product.objects.get(id = pi)
    productsList = ProductsList.objects.filter(product_id=prod, list_id=lis)

    if productsList:
        productsList.delete()
        return HttpResponseRedirect('/')
        
    return HttpResponseRedirect('/')

