# Generated by Django 4.1.3 on 2022-11-22 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BakeCakeBerries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('berry_name', models.CharField(max_length=50, verbose_name='ягода')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('choice_id', models.SmallIntegerField(unique=True, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Ягода',
                'verbose_name_plural': 'Ягоды',
            },
        ),
        migrations.CreateModel(
            name='BakeCakeDecor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decor_name', models.CharField(max_length=50, verbose_name='Декор')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('choice_id', models.SmallIntegerField(unique=True, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Декор',
                'verbose_name_plural': 'Декоры',
            },
        ),
        migrations.CreateModel(
            name='BakeCakeLevels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.SmallIntegerField(verbose_name='Уровень')),
                ('name', models.CharField(max_length=30, verbose_name='Наименование уровня')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('choice_id', models.SmallIntegerField(unique=True, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Уровни тортика',
                'verbose_name_plural': 'Уровни тортиков',
            },
        ),
        migrations.CreateModel(
            name='BakeCakeShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_name', models.CharField(max_length=50, verbose_name='Наименование формы')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('choice_id', models.SmallIntegerField(unique=True, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Форма тортика',
                'verbose_name_plural': 'Формы тортиков',
            },
        ),
        migrations.CreateModel(
            name='BakeCakeTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=100, verbose_name='Название топпинга')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('choice_id', models.SmallIntegerField(unique=True, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Топпинг',
                'verbose_name_plural': 'Топпинги',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BakeCake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inscription', models.CharField(blank=True, max_length=100, null=True, verbose_name='Надпись')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Название')),
                ('berries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.bakecakeberries', verbose_name='Ягоды')),
                ('decor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.bakecakedecor', verbose_name='Декор')),
                ('levels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bakecakelevels', verbose_name='Количество уровней')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bakecakeshape', verbose_name='Форма')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bakecaketopping', verbose_name='Топинг')),
            ],
            options={
                'verbose_name': 'Торт',
                'verbose_name_plural': 'Тортики',
            },
        ),
    ]
