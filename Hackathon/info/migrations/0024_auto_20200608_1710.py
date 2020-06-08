# Generated by Django 3.0.6 on 2020-06-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20200604_2026'),
        ('info', '0023_auto_20200608_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalform',
            name='Problem',
        ),
        migrations.AddField(
            model_name='medicalform',
            name='Problem',
            field=models.ManyToManyField(to='food.Problem'),
        ),
    ]