from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from productcatalog.models import Product


# Create your views here.
def index(request):
	"""
	Rendering the html form as index page
	:param request:
	:return:
	"""
	return render(request, 'productcatalog/index.html')


def storeproduct(request):
	"""
	Storing products in database using a POST request
	:param request:
	:return:
	"""
	productname = request.POST["name"]
	productdescription = request.POST["description"]
	product = Product(name=productname, description=productdescription)
	product.save()
	return HttpResponseRedirect(reverse('productcatalog:index'))


def productlist(request):
	"""
	Getting products from database and rendering in productlist page
	:param request:
	:return:
	"""
	products = Product.objects.all()
	context = {'product_list' : products}
	return render(request, 'productcatalog/productlist.html', context)