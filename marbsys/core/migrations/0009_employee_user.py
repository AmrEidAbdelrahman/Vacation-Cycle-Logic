# Generated by Django 4.0.1 on 2022-01-24 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_alter_officialvacation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(blank=1, null=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=1,
        ),
    ]
