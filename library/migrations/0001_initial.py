# Generated by Django 4.2.3 on 2023-07-05 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0003_student_programme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrowed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_borrowed', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Returned', 'Returned'), ('Not Returned', 'Not Returned')], max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed', to='library.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed', to='students.student')),
            ],
        ),
    ]
