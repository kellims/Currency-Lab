# Generated by Django 4.2.2 on 2023-06-29 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_currency_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money', to='main_app.currency')),
            ],
        ),
    ]
