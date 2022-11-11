from django.contrib.auth.mixins import LoginRequiredMixin
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


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dishes-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dishes-list")


class DishTypeList(generic.ListView):
    model = DishType
    # queryset = DishType.objects.all().select_related("dish")
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-types")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-types")


class CookList(generic.ListView):
    model = Cook
    fields = "__all__"
    paginate_by = 10


class CookDetail(generic.DetailView):
    model = Cook
    fields = "__all__"
    queryset = Cook.objects.all().prefetch_related("dish")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = '__all__'
    success_url = reverse_lazy("kitchen:cooks-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = '__all__'
    success_url = reverse_lazy("kitchen:cooks-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    fields = '__all__'
    success_url = reverse_lazy("kitchen:cooks-list")
