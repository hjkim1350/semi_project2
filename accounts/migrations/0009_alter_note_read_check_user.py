# Generated by Django 3.2.13 on 2022-11-18 01:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_note_read_check_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='read_check_user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='read_check_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
