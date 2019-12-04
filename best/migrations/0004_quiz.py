# Generated by Django 2.2 on 2019-11-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('best', '0003_auto_20191112_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=20)),
                ('option2', models.CharField(max_length=20)),
                ('option3', models.CharField(max_length=20)),
                ('option4', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=25)),
            ],
        ),
    ]