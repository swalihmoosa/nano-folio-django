# Generated by Django 3.2.9 on 2021-12-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=255)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
