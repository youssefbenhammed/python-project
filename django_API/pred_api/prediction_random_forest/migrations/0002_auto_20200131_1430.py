# Generated by Django 3.0.2 on 2020-01-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_random_forest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.FloatField(null=True),
        ),
    ]
