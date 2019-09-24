# Generated by Django 2.2.1 on 2019-09-24 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_subject', models.CharField(help_text='This Field is required', max_length=300)),
                ('todo_details', models.TextField()),
                ('todo_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('check', models.BooleanField(default=False)),
            ],
        ),
    ]