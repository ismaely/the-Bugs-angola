# Generated by Django 4.0.2 on 2023-02-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0009_rename_descricao_imagem_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
