from django.urls import path

from kitchen.views import index, CookList, DishList

urlpatterns = [
    path("", index, name="index"),
    path("cooks/", CookList.as_view(), name="cooks-list"),
    path("dishes/", DishList.as_view(), name="dishes-list")
]


app_name = "kitchen"
