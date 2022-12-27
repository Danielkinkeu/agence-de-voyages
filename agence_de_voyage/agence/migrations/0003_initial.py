# Generated by Django 4.1.2 on 2022-12-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agence', '0002_delete_crud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gestionagence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(default='Daniel', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
    ]