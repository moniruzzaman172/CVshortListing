# Generated by Django 3.2.7 on 2022-11-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authority', '0004_authority'),
    ]

    operations = [
        migrations.CreateModel(
            name='authority_account',
            fields=[
                ('auth_userid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('auth_fullname', models.CharField(max_length=100)),
                ('auth_email', models.CharField(max_length=100)),
                ('auth_pass', models.CharField(max_length=10000)),
                ('auth_phone', models.CharField(max_length=11)),
            ],
        ),
    ]