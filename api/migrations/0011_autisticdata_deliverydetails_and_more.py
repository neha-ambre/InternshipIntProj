# Generated by Django 4.0.4 on 2022-07-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_autisticdata_learning_evaluation_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='autisticdata',
            name='deliveryDetails',
            field=models.CharField(default='NA', max_length=1000),
        ),
        migrations.AddField(
            model_name='autisticdata',
            name='perninantalEventsDetails',
            field=models.CharField(default='NA', max_length=1000),
        ),
    ]
