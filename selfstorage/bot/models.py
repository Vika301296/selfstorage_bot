from django.db import models


class User(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='ФИО')
    telegram_id = models.IntegerField(
        verbose_name='Telegram ID', blank=True, null=True)
    phonenumber = models.CharField(
        'Номер телефона', max_length=20)
    pd_contract = models.FileField(
        verbose_name='Договор об использовании ПД', blank=True, null=True
    )
    storage_unit = models.CharField(
        max_length=20,
        verbose_name='Склад хранения',
        blank=True, null=True)
    box_type = models.CharField(
        max_length=20,
        verbose_name='Вид бокса',
        blank=True, null=True)
    lease_start_date = models.DateTimeField(
        verbose_name='Дата начала аренды',
        blank=True, null=True
    )
    lease_end_date = models.DateTimeField(
        verbose_name='Дата окончания аренды',
        blank=True, null=True
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
