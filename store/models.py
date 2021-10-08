from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.name


class Seller(User):
    business_name = models.CharField(max_length=200)
    business_reg_no = models.CharField (max_length=200, null=False, blank=False)
    phone_number = models.IntegerField()
    external_url =models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name

class Customer(User):
    image =models.ImageField(max_length=255)
    phone_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category =models.ForeignKey('Category',on_delete=models.CASCADE,blank=False, null=False)
    image =models.ImageField(max_length=255) 
    price = models.IntegerField(blank=False, null=False)
    inventory =models.IntegerField(null=False, blank=False)
    seller =models.ForeignKey('Seller',on_delete=models.CASCADE,blank=False, null=False) 
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CustomerAddress(models.Model):
    customer= models.ForeignKey('Customer', on_delete=models.CASCADE, null=False, blank=False) 
    location = models.CharField(max_length=150, blank=False, null=False)
    pin =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
       verbose_name_plural = "Customer Address"

    def __str__(self):
        return self.location

class Order(models.Model):

    ORDER_STATUS = (
        ("pending", "Pending"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        
    )

    cost =models.IntegerField()
    customer =models.ForeignKey('Customer', on_delete=models.CASCADE, null=False, blank=False)
    order_number = models.IntegerField(default =0)
    shipping_cost = models.IntegerField()
    status =models.CharField(max_length=50, blank=True, null=True, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number

class OrderProducts(models.Model):
    product =models.ForeignKey('Product', on_delete=models.CASCADE, null=False, blank=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(blank=False, null=False)
    session =models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Order Products"

    def __str__(self):
        return self.product

class Shipping(models.Model):

    SHIPPING_STATUS =(
        ("pending", "pending"),
        ("dispatched", "dispatched"),
        ("completed", "completed"),
    )
    order= models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=False)
    customer_address = models.ForeignKey(CustomerAddress, on_delete=models.CASCADE, blank=False, null=False)
    status = models.CharField(max_length=50, blank= False, null=True, choices=SHIPPING_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_address

class Payment(models.Model):
    PAYMENT_MODE =(
        ("cash", "cash"),
        ("mpesa", "mpesa"),

    )
    mode = models.CharField(max_length=30, null=False, blank=False, choices=PAYMENT_MODE)
    amount =models.IntegerField()
    order =models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=False)
    invoice_number = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.amount

class Review(models.Model):
    rating =models.IntegerField(blank=True, null=True) 
    message = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating

class Wishlist(models.Model):
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, null=False)
    product =models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product

class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    offer_amount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.offer_amount

class Voucher(models.Model):

    VOURCHER_STATUS =(
        ("active", "active"),
        ("expired", "expired")
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    amount_deducted = models.IntegerField()
    tag =models.CharField(max_length=100)
    status =models.TextField(blank= False, null=True, choices=VOURCHER_STATUS)
    limit =models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tag