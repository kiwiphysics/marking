# Generated by Django 4.2.7 on 2024-01-25 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marking', '0006_alter_standard_q1_type_alter_standard_q2_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades_eemm', models.CharField(default='E8', max_length=2)),
                ('grades_eema', models.CharField(default='E8', max_length=2)),
                ('grades_eemn', models.CharField(default='E8', max_length=2)),
                ('grades_eeaa', models.CharField(default='E8', max_length=2)),
                ('grades_eean', models.CharField(default='E7', max_length=2)),
                ('grades_emma', models.CharField(default='E8', max_length=2)),
                ('grades_emmn', models.CharField(default='E8', max_length=2)),
                ('grades_emaa', models.CharField(default='E8', max_length=2)),
                ('grades_eman', models.CharField(default='E7', max_length=2)),
                ('grades_emnn', models.CharField(default='M5', max_length=2)),
                ('grades_eaaa', models.CharField(default='A4', max_length=2)),
                ('grades_eaan', models.CharField(default='A4', max_length=2)),
                ('grades_eann', models.CharField(default='A4', max_length=2)),
                ('grades_ennn', models.CharField(default='A3', max_length=2)),
                ('grades_mmma', models.CharField(default='M6', max_length=2)),
                ('grades_mmmn', models.CharField(default='M6', max_length=2)),
                ('grades_mmaa', models.CharField(default='M5', max_length=2)),
                ('grades_mman', models.CharField(default='M5', max_length=2)),
                ('grades_mmnn', models.CharField(default='M5', max_length=2)),
                ('grades_maaa', models.CharField(default='A4', max_length=2)),
                ('grades_maan', models.CharField(default='A4', max_length=2)),
                ('grades_mann', models.CharField(default='A3', max_length=2)),
                ('grades_mnnn', models.CharField(default='N2', max_length=2)),
                ('grades_aaaa', models.CharField(default='A4', max_length=2)),
                ('grades_aaan', models.CharField(default='A3', max_length=2)),
                ('grades_aann', models.CharField(default='N2', max_length=2)),
                ('grades_annn', models.CharField(default='N1', max_length=2)),
                ('grades_nnnn', models.CharField(default='N0', max_length=2)),
                ('standard', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='total_standard', to='marking.standard')),
            ],
        ),
    ]
