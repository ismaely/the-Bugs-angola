# Generated by Django 4.0.2 on 2023-03-19 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0015_arquivo_alter_imagem_arquivos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='dataPublicacao',
            field=models.DateField(default=datetime.date(2023, 3, 19)),
        ),
    ]