# Generated by Django 4.1 on 2022-08-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elapp', '0002_elmodel_duedate_elmodel_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='elmodel',
            name='mean',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
