from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    # authenticated user cannot view this view 
    if request.user.is_authenticated:
        return HttpResponseRedirect("/products/")

    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return HttpResponseRedirect("/products/") 

    return render(request, "auth/login.html", { 'form': form }) 

def logout_view(request):
    if request.method == "POST":
       logout(request) 
       return HttpResponseRedirect("/auth/login/")

    return HttpResponseNotAllowed("Unsupported method")