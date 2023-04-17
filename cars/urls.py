from django.urls import path
from cars.views import (
    CarRegisterView,
    CarListView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
)

urlpatterns = [
    path("", CarListView.as_view(), name="cars"),
    path("register/", CarRegisterView.as_view(), name="car_register"),
    path("<int:id>/", CarDetailView.as_view(), name="car_detail"),
    path("<int:id>/update", CarUpdateView.as_view(), name="car_update"),
    path("<int:id>/delete", CarDeleteView.as_view(), name="car_delete"),
]
