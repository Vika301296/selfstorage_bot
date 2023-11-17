# Generated by Django 4.2.7 on 2023-11-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_belongings_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='box_type',
            field=models.CharField(blank=True, max_length=20, verbose_name='Вид бокса'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lease_end_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата окончания аренды'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lease_start_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата начала аренды'),
        ),
        migrations.AlterField(
            model_name='user',
            name='storage_unit',
            field=models.CharField(blank=True, max_length=20, verbose_name='Склад хранения'),
        ),
    ]
