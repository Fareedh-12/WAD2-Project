# Generated by Django 2.2.26 on 2022-03-07 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radar', '0018_userprofile_accept'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId_fk', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='radar.UserProfile')),
            ],
        ),
    ]
