# Generated by Django 4.2 on 2023-05-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recordapp", "0003_alter_saleitem_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="saleitem",
            name="date",
            field=models.CharField(max_length=100),
        ),
    ]
