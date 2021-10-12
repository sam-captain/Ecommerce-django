from django.urls import path
from django.urls.conf import include
from store import views


staff_patterns =[
    path('dashboard', views.dashboard, name="dashboard"),
    path('categories', views.showCategories, name="categories"),
    path('category/form', views.categoryForm, name="add_category"),
    path('store/category', views.storeCategory, name="store_category"),
    path('delete/category/<id>', views.deleteCategory, name="delete_category"),
    path('customers', views.Customer, name="customers" ),
    path('seller', views.Seller, name="sellers"),
    path('seller/form', views.SellerForm, name="sellerform"),
    
]

urlpatterns = [
    path('', views.home, name="home"),
    path('product/', views.product, name="product"),
    path('product_details/', views.ProductDetails, name="product_details"),
    path('cart/', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('categories', views.showCategories, name ="categories"),
    path('staff/', include(staff_patterns)),
     
]