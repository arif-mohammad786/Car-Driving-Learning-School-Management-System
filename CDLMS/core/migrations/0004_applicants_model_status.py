# Generated by Django 3.1.2 on 2020-10-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201011_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants_model',
            name='status',
            field=models.CharField(default='Pending', max_length=255),
        ),
    ]
