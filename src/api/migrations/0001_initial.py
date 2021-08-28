# Generated by Django 3.2.6 on 2021-08-28 17:44

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list_targets', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=list, size=None)),
                ('description', models.TextField(default='', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('list_targets', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=list, size=None)),
                ('end_time_best', models.DateField()),
                ('end_time_actual', models.DateField(null=True)),
                ('finished', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=5, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('status', models.CharField(choices=[('active', 'User that working'), ('fired', 'Fired user'), ('on_holiday', 'User on holiday')], default='active', help_text='User role', max_length=100)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('main', models.BooleanField(default=False)),
                ('telegram', models.CharField(blank=True, max_length=256, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone number. Contains region, and number itself')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.department')),
            ],
        ),
    ]
