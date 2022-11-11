from django import forms


class DishSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)

