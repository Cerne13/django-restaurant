from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Cook, Dish


def index(request):
    cooks = Cook.objects.count()
    dishes = Dish.objects.count()

    context = {
        "num_cooks": cooks,
        "num_dishes": dishes,
    }

    return render(request, "kitchen/index.html", context=context)


class DishList(generic.ListView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class CookList(generic.ListView):
    model = Cook
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")
