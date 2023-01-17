# Generated by Django 4.1.2 on 2023-01-17 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0002_delete_gestionagence'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(choices=[('yaounde', 'yaounde'), ('douala', 'douala'), ('bafoussam', 'bafoussam'), ('dschang', 'dschang'), ('buea', 'buea')], default='lieu de depart', max_length=30)),
                ('destination', models.CharField(choices=[('douala', 'douala'), ('yaounde', 'yaounde'), ('bafoussam', 'bafoussam'), ('dschang', 'dschang'), ('buea', 'buea')], default='lieu de destination', max_length=30)),
                ('datedepart', models.DateField()),
                ('qte', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ReservationForm',
        ),
    ]
