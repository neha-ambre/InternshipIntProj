# Generated by Django 4.0.4 on 2022-06-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_autisticdata_behavior_autisticdata_learning_behavior_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autisticdata',
            name='parenting_style',
            field=models.CharField(default='mixed', max_length=20),
        ),
    ]
