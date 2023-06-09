# Generated by Django 4.2.1 on 2023-05-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolId', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'scl',
            },
        ),
    ]
