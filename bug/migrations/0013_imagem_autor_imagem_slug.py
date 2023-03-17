# Generated by Django 4.0.2 on 2023-03-17 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bug', '0012_remove_imagem_bug'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagem',
            name='slug',
            field=models.SlugField(blank=True, max_length=400, null=True),
        ),
    ]
