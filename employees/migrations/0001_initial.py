# Generated by Django 2.0.6 on 2018-06-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('job_title', models.TextField(blank=True, max_length=255)),
                ('years_experience', models.IntegerField()),
                ('department', models.CharField(choices=[('PR', 'Production'), ('R&D', 'Research and Development'), ('PU', 'Purchasing'), ('MA', 'Marketing'), ('HR', 'Human Resource Management'), ('AC', 'Accounting')], default='PR', max_length=2)),
            ],
        ),
    ]
