# Generated by Django 4.2.7 on 2024-11-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0010_total_grades_eeea_total_grades_eeem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='total',
            name='grades_emmm',
            field=models.CharField(default='E7', max_length=2),
        ),
    ]
