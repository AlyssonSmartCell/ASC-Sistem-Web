# Generated by Django 4.2 on 2023-04-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listadeprecos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pecaeservico', models.TextField(max_length=10)),
                ('valor', models.FloatField()),
            ],
        ),
    ]
