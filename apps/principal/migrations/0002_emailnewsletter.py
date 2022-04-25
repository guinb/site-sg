# Generated by Django 4.0.4 on 2022-04-24 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailNewsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
