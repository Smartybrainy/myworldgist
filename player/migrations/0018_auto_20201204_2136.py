# Generated by Django 3.0.5 on 2020-12-04 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0017_trendingvideo_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrendingVideo',
            new_name='TutorialVideo',
        ),
        migrations.AlterModelOptions(
            name='tutorialvideo',
            options={'verbose_name_plural': 'Tutorial Videos'},
        ),
    ]