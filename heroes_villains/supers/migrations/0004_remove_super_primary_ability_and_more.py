# Generated by Django 4.0.2 on 2022-03-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0003_power_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='primary_ability',
        ),
        migrations.RemoveField(
            model_name='super',
            name='secondary_ability',
        ),
        migrations.AddField(
            model_name='super',
            name='powers',
            field=models.ManyToManyField(to='supers.Power'),
        ),
    ]
