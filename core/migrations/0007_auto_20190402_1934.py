# Generated by Django 2.1.7 on 2019-04-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190331_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetype',
            name='servicetype',
        ),
        migrations.RemoveField(
            model_name='servicetype',
            name='the_choices',
        ),
        migrations.RemoveField(
            model_name='appointement',
            name='service_list',
        ),
        migrations.AlterField(
            model_name='appointement',
            name='when',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
        migrations.DeleteModel(
            name='ServiceType',
        ),
    ]
