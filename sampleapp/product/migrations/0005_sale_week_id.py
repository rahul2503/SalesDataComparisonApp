# Generated by Django 2.2.4 on 2019-08-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20190816_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='week_id',
            field=models.PositiveSmallIntegerField(default=33),
            preserve_default=False,
        ),
    ]
