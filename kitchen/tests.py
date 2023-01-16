from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.forms import CookForm
from kitchen.models import Dish, DishType

PUBLIC_URLS = {
    "HOMEPAGE": reverse("kitchen:index"),
    "COOK_LIST": reverse("kitchen:cooks-list"),
    "DISH_LIST": reverse("kitchen:dishes-list"),
    "DISH_TYPE_LIST": reverse("kitchen:dish-types"),
}

PRIVATE_URLS = {
    "COOK_CREATE": reverse("kitchen:cook-create"),
    "DISH_CREATE": reverse("kitchen:dish-create"),
    "DISH_TYPE_CREATE": reverse("kitchen:dish-type-create"),
}


class PublicViewsTests(TestCase):
    def test_public_pages(self):
        for url in PUBLIC_URLS.values():
            res = self.client.get(url)

            self.assertEqual(res.status_code, 200)

    def test_private_pages(self):
        for url in PRIVATE_URLS.values():
            res = self.client.get(url)

            self.assertNotEqual(res.status_code, 200)


class PrivateViewsTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user", password="1234asdpoi"
        )
        self.client.force_login(self.user)

    def test_private_pages_accessible_for_authenticated(self):
        for url in PRIVATE_URLS.values():
            res = self.client.get(url)

            self.assertEqual(res.status_code, 200)

    def test_dish_creation_successful(self):
        Dish.objects.create(
            name="testfood",
            description="testy and not tasty",
            price=42,
            dish_type_id=1,
        )

        DishType.objects.create(
            name="test_type",
            id=1,
        )

        res = self.client.get(PUBLIC_URLS["DISH_LIST"])
        dishes = Dish.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["dish_list"]),
            list(dishes),
        )


class FormTests(TestCase):
    def test_cook_creation(self):
        data = {
            "username": "test",
            "first_name": "Somename",
            "last_name": "Somelastname",
            "years_of_experience": 5,
        }

        form = CookForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_cook_update_form(self):
        data = {
            "username": "test",
            "first_name": "Somename",
            "last_name": "Somelastname",
            "years_of_experience": 5,
        }

        form = CookForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)
