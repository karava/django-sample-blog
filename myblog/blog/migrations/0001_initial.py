# Generated by Django 3.0.6 on 2020-07-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=170)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=70)),
                ('time', models.TimeField(auto_now=True)),
                ('is_published', models.BooleanField()),
            ],
        ),
    ]
