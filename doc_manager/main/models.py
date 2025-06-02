from django.db import models


class Customer(models.Model):
    """
    Модель заказчика
    """
    name = models.CharField(
        'Наименование заказчика',
        max_length=256
    )

    def __str__(self):
        return self.name


class Object(models.Model):
    """
    Модель объекта
    """
    name = models.CharField(
        'Наименование объекта',
        max_length=256
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    """
    Модель альбома
    """

    class DocType(models.IntegerChoices):
        KJ = 1, 'КЖ'
        KM = 2, 'КМ'
        AR = 3, 'АР'

    customer = models.ForeignKey(
        Customer,
        verbose_name='Заказчик',
        on_delete=models.CASCADE
    )
    object = models.ForeignKey(
        Object,
        verbose_name='объект',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Наименование',
        max_length=256,
        null=True
    )
    doc_type = models.IntegerField(
        choices=DocType.choices,
        verbose_name='Вид документации',
        null=True
    )
    volume = models.FloatField(
        'Объем',
        null=True
    )
    filename = models.CharField(
        'Название файла',
        max_length=256,
        null=True
    )
    inventory_number = models.CharField(
        'Инвентарный номер',
        max_length=50,
        null=True
    )

    def __str__(self):
        return self.name
