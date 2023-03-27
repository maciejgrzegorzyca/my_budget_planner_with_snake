# Generated by Django 4.1.7 on 2023-03-27 17:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('planner', '0006_remove_transactions_is_repatable_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Budgets',
            new_name='Budget',
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='RepeatableTransactions',
            new_name='RepeatableTransaction',
        ),
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
        migrations.RenameModel(
            old_name='Types',
            new_name='Type',
        ),
    ]