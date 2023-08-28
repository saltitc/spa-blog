# Generated by Django 4.2.4 on 2023-08-27 16:29

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tag",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
