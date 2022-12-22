# Generated by Django 3.2.16 on 2022-12-22 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0008_rename_user_adresses_person_user_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_adresses',
            name='is_default',
            field=models.BooleanField(blank=True),
        ),
        migrations.CreateModel(
            name='Credit_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('provider', models.CharField(max_length=20)),
                ('card_number', models.CharField(max_length=16)),
                ('expiration_date', models.DateField()),
                ('security_code', models.CharField(max_length=3)),
                ('is_default', models.BooleanField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
