from rest_framework import serializers

from product.models import Product, Section


class SectionSerializer(serializers.ModelSerializer):
    """Serializer for Section object"""
    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Section
        fields = ('title', 'active', 'products')


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for product object"""
    section = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('title', 'description', 'slug', 'active', 'section')
        read_only_fields = ('slug',)
