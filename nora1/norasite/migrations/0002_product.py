# Generated by Django 5.1 on 2024-08-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('norasite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
