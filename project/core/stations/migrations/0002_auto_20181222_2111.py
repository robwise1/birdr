# Generated by Django 2.1.2 on 2018-12-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='details',
            field=models.TextField(default=''),
        ),
    ]