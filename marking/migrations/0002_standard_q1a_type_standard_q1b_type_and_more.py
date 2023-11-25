# Generated by Django 4.2.7 on 2023-11-12 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard',
            name='q1a_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q1b_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q1c_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q1d_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q2a_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q2b_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q2c_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q2d_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q3a_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q3b_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q3c_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
        migrations.AddField(
            model_name='standard',
            name='q3d_type',
            field=models.CharField(choices=[('A', 'A'), ('M', 'M'), ('E', 'E')], default='A', max_length=2),
        ),
    ]