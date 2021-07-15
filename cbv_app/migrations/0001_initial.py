# Generated by Django 3.1.1 on 2021-07-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('author_name', models.CharField(max_length=30)),
            ],
        ),
    ]