from django.http import HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.views.generic import View

from .forms import ProductForm
from .models import Product

# Create your views here.
class ProductList(LoginRequiredMixin, View):
    def get(self, request):
        user_id = request.user.id
        search = request.GET.get("search","")
        products = Product.objects.filter(user_id=user_id, title__icontains=search)
        return render(request, "products/list.html", { 'products': products, 'search': search })


class ProductCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, "products/create.html", { 'form': form })

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user_id = request.user.id 
            product.save()
            return HttpResponseRedirect("/products/")

        return render(request, "products/create.html", { 'form': form })


class ProductUpdate(LoginRequiredMixin, View):
    def get(self, request, id):
        user_id = request.user.id
        product = get_object_or_404(Product, pk=id, user_id=user_id)
        form = ProductForm(model_to_dict(product))
        return render(request, "products/update.html", { 'form': form })
    
    def post(self, request, id):
        user_id = request.user.id
        product = get_object_or_404(Product, pk=id, user_id=user_id)
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/products/")

        return render(request, "products/update.html", { 'form': form })


class ProductDelete(LoginRequiredMixin, View):
    def post(self, request, id):
        user_id = request.user.id
        product  = get_object_or_404(Product, pk=id, user_id=user_id)
        product.delete()
        return HttpResponseRedirect("/products/")
