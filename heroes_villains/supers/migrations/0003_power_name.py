# Generated by Django 4.0.2 on 2022-03-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0002_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='power',
            name='name',
            field=models.CharField(default='Intelligence', max_length=50),
            preserve_default=False,
        ),
    ]