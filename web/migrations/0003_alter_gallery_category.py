# Generated by Django 3.2.9 on 2021-12-04 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20211204_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.category'),
        ),
    ]
