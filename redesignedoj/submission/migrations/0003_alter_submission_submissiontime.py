# Generated by Django 3.2.12 on 2022-06-30 18:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_alter_submission_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submissionTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
