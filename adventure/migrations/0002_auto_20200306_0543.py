# Generated by Django 3.0.4 on 2020-03-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='uuid',
        ),
        migrations.AddField(
            model_name='room',
            name='x',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='y',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]