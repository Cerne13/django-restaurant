from django.urls import path

from kitchen.views import (
    index,
    CookList,
    DishList,
    CookDetail,
    DishDetail,
    DishTypeList
)


urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookList.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/detail/", CookDetail.as_view(), name="cook-detail"),
    path("dishes/", DishList.as_view(), name="dishes-list"),
    path("dishes/<int:pk>/detail/", DishDetail.as_view(), name="dish-detail"),
    path("dish-types/", DishTypeList.as_view(), name="dish-types")

]


app_name = "kitchen"
