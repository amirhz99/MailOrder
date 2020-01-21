# Generated by Django 3.0.2 on 2020-01-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50, verbose_name='')),
                ('LastName', models.CharField(max_length=50, verbose_name='')),
                ('IdNumber', models.IntegerField()),
                ('PhoneNumber', models.IntegerField()),
                ('WorkPlace', models.CharField(max_length=50, verbose_name='')),
                ('email', models.EmailField(max_length=254, verbose_name='')),
                ('CreateTime', models.DateTimeField(verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 's',
            },
        ),
    ]
