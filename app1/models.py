from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class card(models.Model):
    card_id = models.AutoField
    card_category = models.CharField(max_length=50)
    card_subcategory = models.CharField(max_length=50)
    card_item = models.CharField(max_length=50)
    card_desc = models.CharField(max_length=1000)
    card_price = models.IntegerField(default=0)
    card_date = models.DateField()
    card_image = models.ImageField(upload_to='card/', default='')
    
    def __str__(self):
        return str(self.card_item)
    
State = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Chandigarh','Chandigarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'), 
    ('Haryana','Haryana'), 
    ('Himachal Pradesh','Himachal Pradesh'), 
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'), 
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'), 
    ('Maharashtra','Maharashtra'), 
    ('Manipur','Manipur'), 
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'), 
    ('Nagaland','Nagaland'), 
    ('Odisha','Odisha'), 
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'), 
    ('Tamil Nadu','Tamil Nadu'), 
    ('Telangana','Telangana'), 
    ('Tripura','Tripura'), 
    ('Uttar Pradesh','Uttar Pradesh'),  
    ('West Bengal','West Bengal'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=State, max_length=50)
    pin = models.IntegerField(default=000000)

    def __str__(self):
        return str(self.id)
    
class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    product = models.ForeignKey(card, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

class test(models.Model):
    input1 = models.CharField(max_length=50)
    
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE )
    cart = models.ForeignKey(card, on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=1)






