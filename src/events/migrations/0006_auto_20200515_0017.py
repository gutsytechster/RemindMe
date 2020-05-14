# Generated by Django 2.2.10 on 2020-05-14 18:47

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0005_auto_20200514_2331"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="event_date",
            field=models.DateField(
                default=datetime.datetime(2020, 5, 14, 18, 47, 43, 338494, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event_time",
            field=models.TimeField(
                default=datetime.datetime(2020, 5, 14, 18, 47, 43, 338522, tzinfo=utc)
            ),
        ),
    ]
