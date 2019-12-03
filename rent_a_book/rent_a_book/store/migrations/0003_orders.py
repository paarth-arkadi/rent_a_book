# Generated by Django 2.2.5 on 2019-09-06 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190906_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odemailid', models.CharField(max_length=255)),
                ('purchaseDate', models.DateTimeField(default=datetime.date(2019, 9, 6))),
                ('deliveryDate', models.DateTimeField(default=datetime.date(2019, 9, 9))),
                ('returnDate', models.DateTimeField(default=datetime.date(2019, 9, 20))),
            ],
        ),
    ]