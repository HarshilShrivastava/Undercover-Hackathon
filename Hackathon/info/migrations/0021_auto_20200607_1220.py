# Generated by Django 3.0.6 on 2020-06-07 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0020_dailydiet_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydiet',
            name='Amount',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='dailydiet',
            name='Profile',
            field=models.ForeignKey(default=41, on_delete=django.db.models.deletion.CASCADE, to='info.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailydiet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]