# Generated by Django 3.0.3 on 2020-02-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=True, verbose_name='features'),
            preserve_default=False,
        ),
    ]
