# Generated by Django 5.1.4 on 2025-01-25 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_to', models.CharField(max_length=250)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='L', max_length=1)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
