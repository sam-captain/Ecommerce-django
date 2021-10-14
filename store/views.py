from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, JsonResponse
from .forms import SellerForm, ProductForm


# Create your views here.

def home(request):
     context ={}  

     return render(request, 'store/home.html', context)

def products(request):
     products = Product.objects.all()
     context ={
          'header' : 'This are the products',
          'products' : products
     }

     return render(request, 'store/product.html', context)

def ProductDetails(request):
     products =Product.objects.get(id=product.id)
     context ={
          'products' :products
     }

     return render(request, 'store/product_details.html', context)

def productForm(request):
     form = ProductForm
     context= {
          'ProductForm' : form
     }

     return render(request, 'store/admin/product_form.html', context)
     
def product(request):
     products = Product.objects.all()
     context = {
          'product_list' : products
     }

     return render(request, 'store/admin/product.html', context)



def storeProducts(request):
    Product_name= request.POST.get("name")
    product_category = request.POST.get("category")
    product_image = request.POST.get("image")
    product_price = request.POST.get("price")
    product_iventory = request.POST.get("inventory")
    product_seller = request.POST.get("seller")
    product_description = request.POST.get("description")
    print("category" + product_category)
    
    category = Category.objects.get(pk = int(product_category))
    seller = Seller.objects.get(pk = int(product_seller))


    Product.objects.create(name= Product_name, category=category, image=product_image, price=product_price, inventory=product_iventory,seller=seller, description=product_description)

    return HttpResponseRedirect ("/staff/product")


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
    Category_name = request.POST.get("name")

    Category.objects.create(name= Category_name)

    return HttpResponseRedirect ("/staff/categories")

def deleteCategory(request, id):

    our_category = Category.objects.get(pk=id)

    our_category.delete()

    return HttpResponseRedirect('/staff/categories')
def dashboard(request):
     
     context ={}

     return render(request, 'store/admin/dashboard.html')

def customer(request):
     context ={
          'Sam' : 'Am cool as a developer'
     }
     return render(request, 'store/admin/customers.html', context)


def seller(request):
     seller = Seller.objects.all()
     context ={
          "seller_list" : seller,
     }
     return render(request, 'store/admin/seller.html', context)

def sellerForm(request):
     form = SellerForm()
     context= {
          'SellerForm' : form

     }
     for field in form:
          print(field)
     return render(request, 'store/admin/seller_form.html', context)

def storeSeller(request):
    seller_name = request.POST.get("username")
    business_name = request.POST.get("business_name")
    reg_no = request.POST.get("business_reg_no")
    phone_number = request.POST.get("phone_number")
    external_url =request.POST.get("external_url")

    Seller.objects.create(username= seller_name, business_name=business_name, business_reg_no=reg_no, phone_number =phone_number, external_url= external_url)
    

    return HttpResponseRedirect ("/staff/seller")

    
    
