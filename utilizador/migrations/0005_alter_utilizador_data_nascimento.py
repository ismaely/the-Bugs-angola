# Generated by Django 4.0.2 on 2023-02-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilizador', '0004_alter_utilizador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]