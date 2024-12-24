from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list),
    path("create/", views.product_create),
    path("<int:id>/update/", views.product_update),
    path("<int:id>/delete/", views.product_delete)
]