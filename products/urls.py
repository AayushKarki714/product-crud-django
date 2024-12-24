from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductList.as_view()),
    path("create/", views.ProductCreate.as_view()),
    path("<int:id>/update/", views.ProductUpdate.as_view()),
    path("<int:id>/delete/", views.ProductDelete.as_view())
]