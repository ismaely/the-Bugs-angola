# Generated by Django 4.0.2 on 2023-03-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilizador', '0012_permissao_nao_visivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]