# Generated by Django 5.0.6 on 2024-06-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='apartment_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='building_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='street_two',
            field=models.CharField(max_length=255, null=True),
        ),
    ]