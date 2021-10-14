from django import forms
from .models import Category, Product, Seller




class SellerForm(forms.Form):
    username = forms.CharField(label='your name', max_length=100)
    business_name = forms.CharField(label ='business name', max_length=200)
    business_reg_no = forms.CharField(label ='business number', max_length=200)
    phone_number =forms.CharField(widget= forms.NumberInput)
    external_url = forms.CharField(max_length=200)

class ProductForm(forms.Form):
    name = forms.CharField(label ='name', max_length=200)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    image =forms.ImageField()
    price = forms.IntegerField()
    inventory = forms.IntegerField()
    seller = forms.ModelChoiceField(queryset=Seller.objects.all())
    description = forms.CharField(widget=forms.Textarea)

