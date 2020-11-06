from rest_framework import viewsets

from product.models import Product, Section
from .serializers import ProductSerializer, SectionSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet to retrieve and list products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet to retrieve and list Sections"""
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
