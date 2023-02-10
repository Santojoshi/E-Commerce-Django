from django.contrib import admin
from app1.models import card, cart, Customer, order


admin.site.register(card)
admin.site.register(cart)
admin.site.register(Customer)
admin.site.register(order)

# Register your models here.
