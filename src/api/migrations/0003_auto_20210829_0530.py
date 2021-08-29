# Generated by Django 3.2.6 on 2021-08-29 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.employee'),
        ),
        migrations.AddField(
            model_name='task',
            name='expected_period_days',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
