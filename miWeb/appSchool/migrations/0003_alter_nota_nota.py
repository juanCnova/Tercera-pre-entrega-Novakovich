# Generated by Django 4.1.6 on 2023-03-05 00:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSchool', '0002_rename_estudiantes_estudiante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
