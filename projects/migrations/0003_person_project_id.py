# Generated by Django 3.2.5 on 2021-08-06 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210806_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='project_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
    ]
