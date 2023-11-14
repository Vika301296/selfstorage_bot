from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='ФИО')
    telegram_username = models.CharField(
        max_length=200,
        verbose_name='Аккаунт в телеграмме', blank=True)
    phonenumber = models.CharField(
        'Номер телефона', max_length=20)
    pd_contract = models.FileField(
        verbose_name='Договор об использовании ПД'
    )
    storage_unit = models.CharField(
        max_length=20,
        verbose_name='Склад хранения')
    box_type = models.CharField(
        max_length=20,
        verbose_name='Вид бокса')
    lease_start_date = models.DateTimeField(
        verbose_name='Дата начала аренды'
    )
    lease_end_date = models.DateTimeField(
        verbose_name='Дата окончания аренды'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Belongings(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='belongings',
        verbose_name='Кому принадлежат вещи',
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Cписок вещей')

    class Meta:
        verbose_name = 'Вещи'
    verbose_name_plural = 'Вещи'
