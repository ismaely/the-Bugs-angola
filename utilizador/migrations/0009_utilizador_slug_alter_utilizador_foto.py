# Generated by Django 4.0.2 on 2023-02-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilizador', '0008_utilizador_estadopassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilizador',
            name='slug',
            field=models.SlugField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='foto',
            field=models.ImageField(blank=True, default='user.jpg', null=True, upload_to='uploads/foto/%d-%m-%y/'),
        ),
    ]