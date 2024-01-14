from django.db import models
from django.contrib.auth.models import User   
import uuid

# Create your models here.
class Customer( models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    num_phone = models.TextField(max_length=11)
    def __str__(self):
        return str(self.user)
def generate_cart_id():
    namespace = uuid.UUID('6ba7b811-9dad-11d1-80b4-00c04fd430c8')  
    name = 'cart_id'  
    return str(uuid.uuid5(namespace, name))

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=generate_cart_id, unique=True, editable=False)
    completed = models.BooleanField(default=False)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=10.55)
    description = models.TextField()
    image = models.ImageField()
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=90)
    Zipcode = models.CharField(max_length=10)
class Cartitems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default = 0)