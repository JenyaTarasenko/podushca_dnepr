from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='home'),
    path('product/', views.ProductList.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]