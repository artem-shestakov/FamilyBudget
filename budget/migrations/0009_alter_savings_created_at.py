# Generated by Django 4.0.2 on 2022-03-10 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0008_savings_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savings',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]