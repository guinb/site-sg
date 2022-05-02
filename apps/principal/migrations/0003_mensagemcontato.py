# Generated by Django 4.0.4 on 2022-05-01 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_emailnewsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensagemContato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('empresa', models.CharField(blank=True, max_length=200)),
                ('telefone', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=100)),
                ('interesse', models.CharField(max_length=100)),
                ('mensagem', models.TextField()),
                ('data', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('respondida', models.BooleanField(default=False)),
            ],
        ),
    ]
