# Generated by Django 3.0.3 on 2020-02-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200216_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=True, verbose_name='features'),
        ),
    ]