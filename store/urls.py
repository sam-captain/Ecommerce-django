from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static
from store import views


staff_patterns =[
    path('dashboard', views.dashboard, name="dashboard"),
    path('categories', views.showCategories, name="categories"),
    path('category/form', views.categoryForm, name="add_category"),
    path('store/category', views.storeCategory, name="store_category"),
    path('delete/category/<id>', views.deleteCategory, name="delete_category"),
    path('customers', views.customer, name="customers" ),
    path('seller', views.seller, name="sellers"),
    path('seller/form', views.sellerForm, name="add_seller"),
    path('store/Seller', views.storeSeller, name="store_seller"),
    path('product', views.product, name="product"),
    path('product/form', views.productForm, name="add_product"),
    path('store/product', views.storeProducts, name="store_product"),
    
]

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('product_details/', views.ProductDetails, name="product_details"),
    path('cart/', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('categories', views.showCategories, name ="categories"),
    path('staff/', include(staff_patterns)),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)