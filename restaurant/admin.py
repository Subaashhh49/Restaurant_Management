from django.contrib import admin
from .models import  Category, Menu, Table, Waiter, Order, Reception

# Register your models here.

admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(Waiter)
admin.site.register(Order)
admin.site.register(Reception)
