from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=60)
	product_price = models.DecimalField(max_digits = 10, 
										decimal_places = 2)
	product_description = models.TextField()
	product_weight_value = models.DecimalField(max_digits = 5,
											   decimal_places = 3)
	product_weight_type = models.CharField(max_length=2)
	