# Generated by Django 3.0.3 on 2023-04-05 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('profile', models.ImageField(upload_to='pics')),
                ('img1', models.ImageField(null=True, upload_to='pics')),
                ('img2', models.ImageField(null=True, upload_to='pics')),
                ('description', models.TextField()),
                ('location', models.IntegerField(null=True)),
                ('basePrice', models.IntegerField()),
                ('currentPrice', models.IntegerField()),
                ('minBidPrice', models.IntegerField(null=True)),
                ('tag', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25, null=True)),
                ('sold', models.CharField(default='unsold', max_length=10)),
                ('ownermail', models.EmailField(max_length=254)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('highest_bidder', models.IntegerField(null=True)),
                ('sendwinmail', models.CharField(default='notSent', max_length=7)),
            ],
        ),
    ]
