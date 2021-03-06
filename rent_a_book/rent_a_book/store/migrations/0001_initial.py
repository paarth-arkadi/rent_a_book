# Generated by Django 2.2.5 on 2019-09-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('imageurl', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.CharField(max_length=400)),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]
