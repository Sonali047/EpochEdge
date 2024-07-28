# Generated by Django 4.2.14 on 2024-07-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=200)),
                ('emailAddress', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=20)),
                ('emailSubject', models.CharField(max_length=200)),
                ('emailMessage', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.CharField(max_length=100)),
            ],
        ),
    ]
