# Generated by Django 4.2 on 2023-05-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordapp", "0002_alter_saleitem_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saleitem",
            name="user_id",
            field=models.IntegerField(),
        ),
    ]
