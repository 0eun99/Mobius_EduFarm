# Generated by Django 3.2.7 on 2021-11-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_alter_observe_receive_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observe',
            name='receive_date',
            field=models.CharField(max_length=100),
        ),
    ]
