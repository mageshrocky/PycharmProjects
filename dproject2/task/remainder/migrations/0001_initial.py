# Generated by Django 3.1.7 on 2021-03-18 07:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4)),
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=30)),
                ('task', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=30)),
            ],
        ),
    ]