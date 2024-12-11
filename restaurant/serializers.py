from rest_framework import serializers
from .models import Table, Category, Menu, Order, Waiter, Reception

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Menu
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    table = table = serializers.PrimaryKeyRelatedField(queryset=Table.objects.all())
    waiter = serializers.PrimaryKeyRelatedField(queryset=Waiter.objects.all(), required=False)  
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())


    class Meta:
        model = Order
        fields = '__all__'

class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'
