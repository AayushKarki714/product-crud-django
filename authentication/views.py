from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import View

class Login(LoginView):
    template_name = "auth/login.html"
    next_page = "product_list"
    redirect_authenticated_user = True

# Logout View just call the logout and redirect the user. 
# So no need to subclass any views
class Logout(LoginRequiredMixin, View):
    def post(self, request):
       logout(request) 
       return redirect("login")

