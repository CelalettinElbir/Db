# Generated by Django 3.2.16 on 2022-12-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default='deneme', null=True),
        ),
    ]