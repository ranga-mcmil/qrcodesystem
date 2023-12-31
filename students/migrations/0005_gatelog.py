# Generated by Django 3.2.14 on 2023-07-06 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_oncampus'),
    ]

    operations = [
        migrations.CreateModel(
            name='GateLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.DateTimeField(blank=True, null=True)),
                ('departure', models.DateTimeField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='students.student')),
            ],
        ),
    ]
