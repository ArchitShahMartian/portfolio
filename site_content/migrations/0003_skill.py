# Generated by Django 4.1.3 on 2022-11-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0002_blog_remove_project_created_on_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
            ],
        ),
    ]
