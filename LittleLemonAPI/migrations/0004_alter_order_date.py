# Generated by Django 4.1.4 on 2022-12-31 08:22

import LittleLemonAPI.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0003_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(db_index=True, default=LittleLemonAPI.models.today),
        ),
    ]