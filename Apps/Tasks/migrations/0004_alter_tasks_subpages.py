# Generated by Django 4.1.1 on 2022-09-17 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subpages', '0004_alter_subpages_pages'),
        ('Tasks', '0003_alter_tasks_subpages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='subpages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subpages.subpages'),
        ),
    ]
