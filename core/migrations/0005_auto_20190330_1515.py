# Generated by Django 2.1.7 on 2019-03-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190330_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='servicename',
            field=models.CharField(max_length=50),
        ),
    ]