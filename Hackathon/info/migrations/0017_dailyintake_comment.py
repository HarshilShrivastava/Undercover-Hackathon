# Generated by Django 3.0.6 on 2020-06-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0016_auto_20200607_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyintake',
            name='comment',
            field=models.TextField(default='lllll'),
            preserve_default=False,
        ),
    ]
