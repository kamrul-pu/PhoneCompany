# Generated by Django 4.1.5 on 2023-02-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_primary_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='primary_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]