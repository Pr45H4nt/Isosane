# Generated by Django 4.1.5 on 2023-01-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("idiosaneapp", "0005_alter_article_published_date_alter_article_poster"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="poster",
            field=models.CharField(max_length=10000),
        ),
    ]
