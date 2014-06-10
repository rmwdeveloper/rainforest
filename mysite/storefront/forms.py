from django import forms
from storefront.models import Product

class ProductForm(forms.ModelForm):
	product_name = forms.CharField(label='product_name',widget=forms.TextInput(attrs={'placeholder':'Enter product name',
																					  'id' : 'product_name'}))
	product_price = forms.DecimalField(label='product_price',widget=forms.TextInput(attrs={'placeholder':'Enter product price',
																					  'id' : 'product_price'}))
	product_description = forms.CharField(label='product_description',widget=forms.Textarea
																			(attrs={'placeholder':'Enter product description',
																					  'id' : 'product_description'}))
	product_weight_value = forms.DecimalField(label='product_weight_value',widget=forms.TextInput(attrs={'placeholder':'Enter product weight',
																					  'id' : 'product_weight_value'}))
	product_weight_type = forms.ChoiceField(label='product_weight_type', choices = (('KG','Kilogram(s)'),('LB','Pound(s)')), widget = forms.Select(attrs = {'id': 'product_weight_type'}))
	class Meta:
		model = Product
		fields = ['product_name', 'product_price', 'product_description']