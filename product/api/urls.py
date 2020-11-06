from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('sections', views.SectionViewSet)

app_name = 'product'

urlpatterns = [
    path('', include(router.urls)),
]
