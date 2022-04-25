# Generated by Django 4.0.4 on 2022-04-22 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('empresa', models.CharField(max_length=200)),
                ('respondida', models.BooleanField(default=False)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
