from django.urls import path

from kitchen.views import (
    index,
    CookList,
    DishList,
    CookDetail,
    DishDetail,
    DishTypeList,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView
)

urlpatterns = [
    path("", index, name="index"),

    # Cooks
    path("cooks/", CookList.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/detail/", CookDetail.as_view(), name="cook-detail"),

    # Dishes
    path("dishes/", DishList.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/detail/", DishDetail.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),

    # Dish types
    path("dish-types/", DishTypeList.as_view(), name="dish-types"),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    )

]

app_name = "kitchen"
