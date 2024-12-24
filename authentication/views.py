from django.http import HttpResponseRedirect 
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View

class Login(UserPassesTestMixin, View):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return HttpResponseRedirect('/products/')

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "auth/login.html", { 'form': form }) 

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect("/products/")
        return render(request, "auth/login.html", { 'form': form })



class Logout(LoginRequiredMixin, View):
    def post(self, request):
       logout(request) 
       return HttpResponseRedirect("/auth/login/")

