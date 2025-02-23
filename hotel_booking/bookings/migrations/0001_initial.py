# Generated by Django 4.2.16 on 2024-09-10 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('room_type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')], max_length=10)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='room_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bookings.room')),
                ('users', models.ManyToManyField(related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
