# Generated by Django 5.2.1 on 2025-06-01 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='invenroty_number',
            field=models.CharField(max_length=50, null=True, verbose_name='Инвентарный номер'),
        ),
    ]
