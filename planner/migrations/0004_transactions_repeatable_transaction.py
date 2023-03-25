# Generated by Django 4.1.7 on 2023-03-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("planner", "0003_repeatabletransactions_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactions",
            name="repeatable_transaction",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="planner.repeatabletransactions",
            ),
            preserve_default=False,
        ),
    ]