# from django.shortcuts import get_object_or_404, render, redirect
# from django.views import View
# from django.forms.models import model_to_dict
from cars.forms import CarForm
from cars.models import Car
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# class CarRegisterView(View):
#     def get(self, req):
#         form = CarForm()
#         context = {"form": form}
#         return render(req, "register_car.html", context)

#     def post(self, req):
#         form = CarForm(req.POST)

#         if form.is_valid():
#             form_data = form.cleaned_data
#             Car.objects.create(**form_data)
#             return redirect("/cars/")


#         context = {"form": form}
#         return render(req, "register_car.html", context)
class CarRegisterView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "register_car.html"
    success_url = "/cars/"


# class CarListView(View):
#     def get(self, req):
#         cars = Car.objects.all()
#         cars = [model_to_dict(car) for car in cars]


#         context = {"cars": cars}
#         return render(req, "cars.html", context)


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"


# class CarDetailView(View):
#     def get(self, req, id):
#         car = Car.objects.filter(id=id).first()

#         if not car:
#             return redirect("/cars/")


#         context = {"car": model_to_dict(car)}
#         return render(req, "car_detail.html", context)
class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"
    pk_url_kwarg = "id"


# class CarUpdateView(View):
#     def get(self, req, id):
#         car = Car.objects.filter(id=id).first()

#         if not car:
#             return redirect("/cars/")

#         form = CarForm(
#             initial={
#                 "brand": car.brand,
#                 "model": car.model,
#                 "color": car.color,
#                 "year": car.year,
#             }
#         )

#         context = {"form": form}

#         return render(req, "update_car.html", context)

#     def post(self, req, id):
#         car = Car.objects.filter(id=id).first()

#         if not car:
#             return redirect("/cars/")

#         form = CarForm(
#             req.POST,
#             initial={
#                 "brand": car.brand,
#                 "model": car.model,
#                 "color": car.color,
#                 "year": car.year,
#             },
#         )

#         if form.is_valid():
#             for key, value in form.cleaned_data.items():
#                 setattr(car, key, value)
#             car.save()
#             return redirect("/cars/")

#         context = {"form": form}


#         return render(req, "update_car.html", context)
class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = "update_car.html"
    form_class = CarForm
    pk_url_kwarg = "id"
    success_url = "/cars/"


# class CarDeleteView(View):
#     def get(self, req, id):
#         car = get_object_or_404(Car, id=id)
#         car.delete()
#         return redirect("/cars/")
class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "car_delete.html"
    pk_url_kwarg = "id"
    success_url = "/cars/"
