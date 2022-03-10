# Generated by Django 4.0.2 on 2022-03-10 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0007_alter_incomes_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='savings',
            name='wallet',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.PROTECT, to='budget.wallet'),
            preserve_default=False,
        ),
    ]