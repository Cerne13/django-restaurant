from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Cook, Dish, DishType


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
    paginate_by = 10


class DishDetail(generic.DetailView):
    model = Dish
    fields = "__all__"
    queryset = Dish.objects.all().prefetch_related("cooks")


class DishTypeList(generic.ListView):
    model = DishType
    # queryset = DishType.objects.all().select_related("dish")
    template_name = "dish_type_list.html"
    context_object_name = "dish_type_list"


class CookList(generic.ListView):
    model = Cook
    fields = "__all__"
    paginate_by = 10


class CookDetail(generic.DetailView):
    model = Cook
    fields = "__all__"
    queryset = Cook.objects.all().prefetch_related("dish")
