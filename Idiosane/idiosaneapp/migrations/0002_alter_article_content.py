# Generated by Django 4.1 on 2023-01-10 06:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("idiosaneapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="Content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
