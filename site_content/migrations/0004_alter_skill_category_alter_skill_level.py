# Generated by Django 4.1.3 on 2022-11-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0003_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.IntegerField(null=True),
        ),
    ]
