# Generated by Django 3.0.5 on 2020-12-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201205_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillist',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]