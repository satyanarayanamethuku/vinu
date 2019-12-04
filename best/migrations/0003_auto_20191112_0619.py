# Generated by Django 2.2 on 2019-11-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0002_bhim_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='bhim_app',
            name='email',
            field=models.EmailField(default=2, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bhim_app',
            name='full_name',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
    ]