# Generated by Django 3.2.9 on 2022-02-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_requisition_app', '0020_auto_20220207_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrequisition',
            name='request_status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]