# Generated by Django 4.2 on 2023-05-02 12:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recordapp", "0004_alter_saleitem_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="saleitem",
            old_name="date",
            new_name="date_str",
        ),
    ]
