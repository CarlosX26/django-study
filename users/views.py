# from django.forms import model_to_dict
# from django.shortcuts import render
# from django.views import View
# from django.core import serializers
# from django.http import HttpResponse, JsonResponse
from users.models import User
from users.forms import UserForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


# class ListUserView(View):
#     def get(self, req):
#         return JsonResponse({"message": "hello django"})

#     def get(self, req):
#         users = serializers.serialize("python", User.objects.all(), fields=("username"))
#         users = [user["fields"] for user in users]

#         context = {"users": users}


#         return render(req, "list_users.html", context)
class ListUserView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = "users"
    template_name = "list_users.html"


# class RegisterUserView(View):
#     def get(self, request):
#         form = RegisterUserForm()
#         context = {"form": form}
#         return render(request, "register_users.html", context)

#     def post(self, req):
#         form = RegisterUserForm(req.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data

#         user = User.objects.create_user(**form_data)


#         return render(req, "user_created.html", {"user": model_to_dict(user)})
class RegisterUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = "register_users.html"
    success_url = "/users/login/"


class LoginView(LoginView):
    template_name = "login.html"
    success_url = "/cars/"
