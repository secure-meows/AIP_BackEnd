# Generated by Django 2.2.3 on 2019-07-11 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aipsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aipuser',
            name='classno',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='aipsite.PublicKey', to_field='classno'),
        ),
        migrations.AlterField(
            model_name='aipuser',
            name='is_signed',
            field=models.BooleanField(default=False),
        ),
    ]
