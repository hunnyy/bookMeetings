# Generated by Django 3.0.4 on 2020-03-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200313_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Roomname', models.CharField(max_length=100)),
                ('CreditsPerHr', models.CharField(max_length=10)),
                ('Capacity', models.CharField(max_length=10)),
                ('Property', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='companyregister',
            old_name='Name',
            new_name='name',
        ),
    ]
