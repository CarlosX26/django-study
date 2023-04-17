from django.urls import path
from users.views import ListUserView, RegisterUserView, LoginView

urlpatterns = [
    path("", ListUserView.as_view()),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view()),
]
