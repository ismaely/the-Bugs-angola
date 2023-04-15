# Generated by Django 4.0.2 on 2023-04-14 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0017_alter_imagem_datapublicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='miniDescricao',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='uploads/arquivo/%d-%m-%Y/'),
        ),
        migrations.AlterField(
            model_name='arquivo',
            name='bug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='bug.bug'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='arquivos',
            field=models.FileField(blank=True, null=True, upload_to='uploads/imagem/%d-%m-%Y/'),
        ),
    ]