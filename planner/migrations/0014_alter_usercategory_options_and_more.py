# Generated by Django 4.1.7 on 2023-04-06 14:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0013_category_default_usercategory_category_sers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="usercategory",
            options={
                "verbose_name": "User Category",
                "verbose_name_plural": "User Categories",
            },
        ),
        migrations.RenameField(
            model_name="category",
            old_name="sers",
            new_name="users",
        ),
    ]
