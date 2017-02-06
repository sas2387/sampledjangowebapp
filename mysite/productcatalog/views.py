from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from productcatalog.models import Product

# Create your views here.
def index(request):
	return render(request, 'productcatalog/index.html')

def storeproduct(request):
	product = Product.objects.create(request.POST["productname"], request.POST["description"])
	return HttpResponseRedirect(reverse('productcatalog:index'))

def productlist(request):
	products = Product.objects.all()
	context = {'product_list' : products}
	return render(request, 'productcatalog/productlist.html', context)

def productdetail(request):
	return render(request, 'productcatalog/productdetail.html')