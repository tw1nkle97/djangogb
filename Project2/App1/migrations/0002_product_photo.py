# Generated by Django 5.0.1 on 2024-02-25 14:14

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App1", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    base_url="/media", location="../media"
                ),
                upload_to="product_photos/",
            ),
        ),
    ]
