from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse

# Create your views here.

def home(request):
     context ={}  

     return render(request, 'store/home.html', context)

def product(request):
     context ={}

     return render(request, 'store/product.html', context)

def ProductDetails(request):
     context ={}

     return render(request, 'store/product_details.html', context)

def cart(request):
     context ={}

     return render(request, 'store/cart.html', context)

def checkout(request):
     context= {}
     return render(request, 'store/checkout.html', context)

def showCategories(request):
    context = {
        'category_list': Category.objects.all()
    }
    return render(request, "store/admin/categories.html", context)

def categoryForm(request):
    context ={}
    return render(request, "store/admin/categories_form.html", context)

def storeCategory(request):
    Category_name = request.Product.get("name")

    Category.objects.create(name= Category_name)

    return HttpResponseRedirect ("/staff/categories")

def deleteCategory(request, id):

    our_category = Category.objects.get(pk=id)

    our_category.delete()

    return HttpResponseRedirect('/staff/categories')
def dashboard(request):
     
     context ={}

     return render(request, 'store/admin/dashboard.html')

def Customer(request):
     context ={
          'Sam' : 'Am cool as a developer'
     }
     return render(request, 'store/admin/customers.html', context)

    
    
