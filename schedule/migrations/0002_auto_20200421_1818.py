# Generated by Django 2.2.4 on 2020-04-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]