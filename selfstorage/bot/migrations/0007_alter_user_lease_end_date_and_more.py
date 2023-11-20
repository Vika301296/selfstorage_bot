# Generated by Django 4.2.7 on 2023-11-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0006_alter_box_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="lease_end_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата окончания аренды"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="lease_start_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Дата начала аренды"
            ),
        ),
    ]
