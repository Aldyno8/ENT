# Generated by Django 5.0.7 on 2024-07-28 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0009_alter_documents_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='Course',
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Duration', models.IntegerField()),
                ('Credit', models.IntegerField()),
                ('Students', models.ManyToManyField(blank=True, related_name='modules', to='Students.students')),
            ],
        ),
        migrations.AddField(
            model_name='documents',
            name='Modules',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='Students.modules'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
