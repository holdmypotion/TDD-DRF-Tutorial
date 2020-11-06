from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from product.models import Product, Section
from product.api.serializers import ProductSerializer, SectionSerializer


PRODUCT_URL = reverse('product:product-list')
SECTION_URL = reverse('product:section-list')


def detail_url(product_id):
    """Returns product detail URL"""
    return reverse('product:product-detail', args=[product_id])


def sample_section(**params):
    """Section Section"""
    defaults = {'title': 'SampleSection'}
    defaults.update(params)

    return Section.objects.create(**defaults)


def sample_product(**params):
    """Sample Product"""
    section = sample_section()
    defaults = {
        'title': 'SampleProduct',
        'slug': 'sampleproduct'
    }
    defaults.update(params)  # For overriding the defaults with the params

    return Product.objects.create(section=section, **defaults)


class PublicProductApiTest(TestCase):
    """Test the publically available Product API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_products(self):
        """Test retrieving products"""
        sample_product()
        sample_product(slug='sampleproduct2')

        res = self.client.get(PRODUCT_URL)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_product_detail(self):
        """Test viewing a product detail"""
        product = sample_product(description='This is a tape, ofcourse')

        url = detail_url(product.id)
        res = self.client.get(url)

        serializer = ProductSerializer(product)
        self.assertEqual(res.data, serializer.data)


class PublicSectionApiTest(TestCase):
    """Test the publically available Section API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_section(self):
        """Test retrieving products"""
        sample_section()
        sample_section(title='Sample 2')

        res = self.client.get(SECTION_URL)

        sections = Section.objects.all()
        serializer = SectionSerializer(sections, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
