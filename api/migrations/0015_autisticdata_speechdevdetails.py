# Generated by Django 4.0.4 on 2022-07-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_autisticdata_delayed_speech_developement'),
    ]

    operations = [
        migrations.AddField(
            model_name='autisticdata',
            name='speechDevDetails',
            field=models.TextField(default='NA'),
        ),
    ]
