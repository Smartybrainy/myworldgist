# Generated by Django 3.0.5 on 2020-09-04 01:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200904_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 9, 4, 1, 10, 52, 313949, tzinfo=utc)),
        ),
    ]