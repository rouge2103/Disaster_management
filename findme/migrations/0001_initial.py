# Generated by Django 3.1 on 2020-11-23 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('fathers_name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=120)),
                ('latitude', models.CharField(max_length=120)),
                ('longitude', models.CharField(max_length=120)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
