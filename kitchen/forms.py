from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from kitchen.models import Cook, Dish


def validate_experience(years):
    if years > 40:
        raise ValidationError("Experience can not be more than 40 years")
    if years < 1:
        raise ValidationError("We need experience chef on the kitchen")

    return years


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        return validate_experience(self.cleaned_data["years_of_experience"])


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter a dish name"}),
    )


class DishTypeSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter a dish type name"}),
    )


class CookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter a cook's name"}),
    )
