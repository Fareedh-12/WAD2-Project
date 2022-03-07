# Generated by Django 2.2.26 on 2022-03-07 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('host', models.BooleanField(default=False)),
                ('age', models.IntegerField(default=0)),
                ('shareLocation', models.BooleanField(default=False)),
                ('request', models.BooleanField(default=False)),
                ('accept', models.BooleanField(verbose_name=False)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.BooleanField(default=True)),
                ('hasArrived', models.BooleanField(default=False)),
                ('destination', models.CharField(max_length=128, unique=True)),
                ('userId_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radar.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendId_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radar.UserProfile')),
            ],
        ),
    ]
