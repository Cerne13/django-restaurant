# Generated by Django 4.1.3 on 2022-11-13 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["name"], "verbose_name_plural": "dishes"},
        ),
        migrations.AlterField(
            model_name="dish",
            name="dish_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dish",
                to="kitchen.dishtype",
            ),
        ),
    ]