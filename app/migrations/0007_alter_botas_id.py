# Generated by Django 4.1.1 on 2022-11-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20221122_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
