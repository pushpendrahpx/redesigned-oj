# Generated by Django 3.2.12 on 2022-07-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_alter_submission_submissiontime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='usercode',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='useroutput',
        ),
        migrations.AddField(
            model_name='submission',
            name='usersubmissionfile',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
