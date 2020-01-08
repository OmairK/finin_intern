# Generated by Django 3.0.2 on 2020-01-08 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_sessions.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('finin_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mobile_number', models.BigIntegerField(verbose_name='mobile number')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', user_sessions.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSessions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('date_time_of_session_start', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='session active')),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]