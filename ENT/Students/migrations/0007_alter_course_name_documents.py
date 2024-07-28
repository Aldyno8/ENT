# Generated by Django 5.0.7 on 2024-07-28 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0006_rename_bith_students_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=150)),
                ('Course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Students.course')),
            ],
        ),
    ]
