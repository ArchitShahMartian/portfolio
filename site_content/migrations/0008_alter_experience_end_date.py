# Generated by Django 4.1.3 on 2022-11-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0007_remove_experience_time_range_experience_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]