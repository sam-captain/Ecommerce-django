from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(CustomerAddress)
admin.site.register(Order)
admin.site.register(OrderProducts)
admin.site.register(Shipping)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Voucher)