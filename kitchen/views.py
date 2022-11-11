from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishSearchForm, CookSearchForm, DishTypeSearchForm
from kitchen.models import Cook, Dish, DishType


def index(request):
    cooks = Cook.objects.count()
    dishes = Dish.objects.count()

    context = {
        "num_cooks": cooks,
        "num_dishes": dishes,
    }

    return render(request, "kitchen/index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = DishSearchForm(initial={
            "title": title
        })
        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["title"])

        return self.queryset


class DishDetailView(generic.DetailView):
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


class DishTypeListView(generic.ListView):
    model = DishType
    paginate_by = 5
    queryset = DishType.objects.all()
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = DishTypeSearchForm(initial={
            "title": title
        })
        return context

    def get_queryset(self):
        title = self.request.GET.get("title")

        if title:
            return self.queryset.filter(name__icontains=title)

        return self.queryset


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


class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.all()
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = CookSearchForm(initial={
            "title": title
        })
        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(first_name__icontains=form.cleaned_data["title"])

        return self.queryset


class CookDetailView(generic.DetailView):
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
