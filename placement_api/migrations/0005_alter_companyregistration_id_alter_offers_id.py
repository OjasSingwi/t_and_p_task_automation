# Generated by Django 5.1.1 on 2024-12-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_api', '0004_alter_companyregistration_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyregistration',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='offers',
            name='id',
            field=models.UUIDField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
