# Generated by Django 2.2.3 on 2019-07-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=500)),
                ('b', models.CharField(max_length=500)),
                ('c', models.CharField(max_length=500)),
                ('n', models.CharField(max_length=500)),
                ('g', models.CharField(max_length=500)),
                ('h', models.CharField(max_length=500)),
                ('p', models.CharField(max_length=500)),
                ('classno', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]