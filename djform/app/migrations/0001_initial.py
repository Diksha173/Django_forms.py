# Generated by Django 5.0.2 on 2024-03-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('sage', models.IntegerField()),
                ('saddress', models.CharField(max_length=50)),
                ('spassword', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('cource', models.CharField(max_length=50)),
            ],
        ),
    ]