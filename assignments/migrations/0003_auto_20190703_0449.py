# Generated by Django 2.2.2 on 2019-07-03 02:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_auto_20190703_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 3, 2, 49, 37, 845740, tzinfo=utc)),
        ),
    ]
