from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

from .forms import ProductForm
from .models import Product

# Create your views here.
@login_required
def product_list(request):
    user_id = request.user.id
    search = request.GET.get("search","")
    products = Product.objects.filter(user_id=user_id, title__icontains=search)
    return render(request, "products/list.html", { 'products': products, 'search': search })


@login_required
def product_create(request):
    if request.method == "GET":
        form = ProductForm()
    elif request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user_id = request.user.id 
            product.save()
            return HttpResponseRedirect("/products/")

    return render(request, "products/create.html", { 'form': form })

@login_required
def product_update(request, id):
    user_id = request.user.id
    product = get_object_or_404(Product, pk=id, user_id=user_id)

    if request.method == "GET":
        form = ProductForm(model_to_dict(product))

    elif request.method == "POST":
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/products/")

    return render(request, "products/update.html", { 'form': form })

@login_required
def product_delete(request, id):
    user_id = request.user.id

    if request.method == "POST":
        product  = get_object_or_404(Product, pk=id, user_id=user_id)
        product.delete()
        return HttpResponseRedirect("/products/")

    return HttpResponseNotAllowed("Unsupported http method")