# Generated by Django 4.2.3 on 2023-07-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='programme',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
