# Generated by Django 2.1.11 on 2019-12-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0012_teststatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='FastCheckDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('errorInfo', models.TextField()),
            ],
            options={
                'db_table': 'FastCheckDetail',
            },
        ),
        migrations.CreateModel(
            name='JsCssCheckInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.TimeField()),
                ('endTiem', models.TimeField()),
                ('checkFileNum', models.IntegerField()),
                ('errorFileNum', models.IntegerField()),
                ('checkFile', models.TextField()),
            ],
            options={
                'db_table': 'JsCssCheckInfo',
            },
        ),
    ]
