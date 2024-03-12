from django.urls import path
from .views import multiply
from simpleapp.views import ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
# from .views import ProductsList, ProductDetail


urlpatterns = [
   path('', ProductsList.as_view(), name='product_list'),
   path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
   path('multiply/', multiply),
   path('create/', ProductCreate.as_view(), name='product_create'),
   path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]