# Generated by Django 5.0.7 on 2024-07-28 12:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Niveau', models.CharField(choices=[('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3')], default='L1', max_length=3)),
                ('Parcours', models.CharField(choices=[('RSI', 'RSI'), ('IDEV', 'IDEV')], default='IDEV', max_length=5)),
                ('Age', models.IntegerField()),
                ('Bith', models.DateField()),
                ('Inscription', models.DateField()),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Duration', models.IntegerField()),
                ('Credit', models.IntegerField()),
                ('Students', models.ManyToManyField(to='Students.students')),
            ],
        ),
    ]
