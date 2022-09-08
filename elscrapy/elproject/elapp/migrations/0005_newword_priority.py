# Generated by Django 4.1 on 2022-09-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elapp', '0004_newword_mean'),
    ]

    operations = [
        migrations.AddField(
            model_name='newword',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('info', 'middle'), ('success', 'low')], max_length=50, null=True),
        ),
    ]
