from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductList.as_view(), name="product_list"),
    path("create/", views.ProductCreate.as_view(), name="product_create"),
    path("<int:id>/update/", views.ProductUpdate.as_view(), name="product_update"),
    path("<int:id>/delete/", views.ProductDelete.as_view(), name="product_delete")
]
