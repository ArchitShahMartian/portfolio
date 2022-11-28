# Generated by Django 4.1.3 on 2022-11-26 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('last_updated_at', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='project',
            name='last_updated_at',
        ),
    ]