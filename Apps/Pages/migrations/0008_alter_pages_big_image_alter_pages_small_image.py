# Generated by Django 4.1.1 on 2022-09-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0007_remove_pages_tat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='big_image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='pages',
            name='small_image',
            field=models.CharField(max_length=500),
        ),
    ]
