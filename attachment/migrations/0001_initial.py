# Generated by Django 2.2.12 on 2020-05-11 00:18

import attachment.base_models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=attachment.base_models.MediaFileSystemStorage(), upload_to='files', verbose_name='File')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('download_key', models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=16)),
                ('owner_groups', models.ManyToManyField(blank=True, to='auth.Group')),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
