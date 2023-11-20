from django.db import models


class Storage(models.Model):
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес'
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Хранилище'
        verbose_name_plural = 'Адрес хранилища'


class Box(models.Model):
    size = models.PositiveSmallIntegerField(
        verbose_name='Размер бокса'
    )
    address = models.ForeignKey(
        Storage,
        verbose_name='Адрес',
        related_name='box',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_occupied = models.BooleanField(
        default=False
    )
    current_renter = models.ForeignKey(
        'User',
        related_name='rented_boxes',
        verbose_name='Текущий арендатор',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Бокс под номером {self.id} имеет размер: {self.size} м2"

    class Meta:
        verbose_name = 'Бокс'
        verbose_name_plural = 'Боксы'


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
    rented_box = models.ForeignKey(
        Box,
        related_name='renters',
        verbose_name='Арендованный бокс',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    lease_start_date = models.DateField(
        verbose_name='Дата начала аренды',
        blank=True, null=True
    )
    lease_end_date = models.DateField(
        verbose_name='Дата окончания аренды',
        blank=True, null=True
    )

    def __str__(self):
        return self.name

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
    box = models.ForeignKey(
        Box,
        related_name='belongings',
        verbose_name='Бокс',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.owner} владеет: {self.description}"

    class Meta:
        verbose_name = 'Вещи'
        verbose_name_plural = 'Вещи'
