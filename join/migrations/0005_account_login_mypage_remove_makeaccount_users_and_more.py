# Generated by Django 4.2.7 on 2023-11-23 17:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0004_makeaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='mypage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='makeaccount',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='studentId',
            field=models.IntegerField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='loginout',
        ),
        migrations.DeleteModel(
            name='makeaccount',
        ),
        migrations.AddField(
            model_name='mypage',
            name='users',
            field=models.ManyToManyField(related_name='mypage', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='login',
            name='users',
            field=models.ManyToManyField(related_name='login', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='users',
            field=models.ManyToManyField(related_name='account', to=settings.AUTH_USER_MODEL),
        ),
    ]
