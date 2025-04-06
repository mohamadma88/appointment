# Generated by Django 5.1.7 on 2025-04-06 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='روز')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی بیمار')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تلفن')),
                ('time', models.TimeField(verbose_name='ساعت')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor', verbose_name='دکتر')),
                ('day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='day', to='appointment.appointmentday', verbose_name='روز')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
    ]
