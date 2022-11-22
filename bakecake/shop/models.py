from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


# Тут описываем свою модель пользователя
class AppUser(AbstractUser):
    pass


class BakeCakeLevels(models.Model):
    level = models.SmallIntegerField('Уровень')
    name = models.CharField('Наименование уровня', max_length=30)
    price = models.FloatField('Цена')
    choice_id = models.SmallIntegerField('Номер', unique=True)

    class Meta:
        verbose_name = 'Уровни тортика'
        verbose_name_plural = 'Уровни тортиков'

    def __str__(self):
        return f'{self.choice_id}. {self.name} : {str(self.price)} Руб.'


class BakeCakeShape(models.Model):
    shape_name = models.CharField('Наименование формы', max_length=50)
    price = models.FloatField('Цена')
    choice_id = models.SmallIntegerField('Номер', unique=True)

    class Meta:
        verbose_name = 'Форма тортика'
        verbose_name_plural = 'Формы тортиков'

    def __str__(self):
        return f'{self.choice_id}. {self.shape_name} : {str(self.price)} Руб.'


class BakeCakeTopping(models.Model):
    topping_name = models.CharField('Название топпинга', max_length=100)
    price = models.FloatField('Цена')
    choice_id = models.SmallIntegerField('Номер', unique=True)

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return f'{self.choice_id}. {self.topping_name} : {str(self.price)} Руб.'


class BakeCakeBerries(models.Model):
    berry_name = models.CharField('ягода', max_length=50)
    price = models.FloatField('Цена')
    choice_id = models.SmallIntegerField('Номер', unique=True)

    class Meta:
        verbose_name = 'Ягода'
        verbose_name_plural = 'Ягоды'

    def __str__(self):
        return f'{self.choice_id}. {self.berry_name} : {str(self.price)} Руб.'


class BakeCakeDecor(models.Model):
    decor_name = models.CharField('Декор', max_length=50)
    price = models.FloatField('Цена')
    choice_id = models.SmallIntegerField('Номер', unique=True)

    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декоры'

    def __str__(self):
        return f'{self.choice_id}. {self.decor_name} : {str(self.price)} Руб.'


# Модель тортика
class BakeCake(models.Model):

    levels = models.ForeignKey('BakeCakeLevels', verbose_name='Количество уровней', on_delete=models.CASCADE)
    shape = models.ForeignKey('BakeCakeShape', verbose_name='Форма', on_delete=models.CASCADE)
    topping = models.ForeignKey('BakeCakeTopping', verbose_name='Топинг', on_delete=models.CASCADE)
    berries = models.ForeignKey('BakeCakeBerries', verbose_name='Ягоды', on_delete=models.CASCADE, blank=True, null=True)
    decor = models.ForeignKey('BakeCakeDecor', verbose_name='Декор', on_delete=models.CASCADE, blank=True, null=True)
    inscription = models.CharField('Надпись', max_length=100, blank=True, null=True)
    name = models.CharField('Название', max_length=100, blank=True)
    image = models.ImageField('Изображение', upload_to='media/BakeCakeImages/', blank=True, null=True, default='media/BakeCakeImages/no_image.png')
    catalog = models.ForeignKey('Catalog', verbose_name='В каталоге', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Тортики'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.pk)

    def get_absolute_url(self):
        return reverse('bakecake-detail', kwargs={'pk': self.pk})


# Модель заказа тортика
class Order(models.Model):
    ...


# Модель каталога тортиков
class Catalog(models.Model):
    name = models.CharField('Название', max_length=50, default='На чаепитие')
    image = models.ImageField('Изображение', upload_to='media/catalog/', default='media/BakeCakeImages/no_image.png')

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name
