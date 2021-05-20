from django.urls import path,include
from . import views
from .views import ProductsApi,CategoryApi,StockApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ProductsApi',views.ProductsApi,)
router.register('StockApi',views.StockApi,)
router.register('CategoryApi',views.CategoryApi,)


urlpatterns = [
    
    path('',include(router.urls)),
    
]
