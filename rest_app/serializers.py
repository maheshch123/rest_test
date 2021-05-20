from rest_framework import serializers
from .models import Product,Category,Stock

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['stock'] = StockSerializers(instance.stock).data
        return response

class StockSerializers(serializers.ModelSerializer):
    products = ProductSerializers(read_only=True)
    
    class Meta:
        model = Stock
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    products = ProductSerializers(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['products'] = ProductSerializers(instance.products).data
    #     return response