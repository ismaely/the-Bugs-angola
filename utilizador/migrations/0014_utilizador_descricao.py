# Generated by Django 4.0.2 on 2023-03-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilizador', '0013_alter_utilizador_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='descricao',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
    ]
