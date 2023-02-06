# Generated by Django 4.0.2 on 2023-02-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0004_remove_imagem_data_remove_imagem_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='arquivos',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%d-%m-%yyyy/'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
