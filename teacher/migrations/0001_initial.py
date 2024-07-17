# Generated by Django 5.0.7 on 2024-07-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=20)),
                ('staff_id', models.CharField(max_length=20)),
            ],
        ),
    ]