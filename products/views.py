from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product

# Create your views here.
class ProductList(LoginRequiredMixin, ListView):
    template_name = "products/list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        return context

    def get_queryset(self):
        user_id = self.request.user.id
        search = self.request.GET.get("search","")
        products = Product.objects.filter(user_id=user_id, title__icontains=search)
        return products 


class ProductCreate(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = "products/create.html"
    success_url = reverse_lazy("product_list")
    
    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)


class ProductUpdate(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    template_name = "products/update.html"
    success_url = reverse_lazy("product_list")

    def get_object(self):
        user_id = self.request.user.id
        pk = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Product, pk=pk, user_id=user_id)


class ProductDelete(LoginRequiredMixin, View):
    def post(self, request, pk):
        user_id = request.user.id
        product  = get_object_or_404(Product, pk=pk, user_id=user_id)
        product.delete()
        return redirect("product_list")
