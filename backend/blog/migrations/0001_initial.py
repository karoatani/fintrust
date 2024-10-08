# Generated by Django 5.1.1 on 2024-09-15 20:03

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TableOfContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reply",
                        to="blog.comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("body", django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text")),
                ("is_archive", models.BooleanField(default=False)),
                ("is_draft", models.BooleanField(default=False)),
                ("views", models.PositiveBigIntegerField()),
                ("likes", models.PositiveBigIntegerField()),
                ("dislikes", models.PositiveBigIntegerField()),
                ("cover_image", models.ImageField(upload_to="cover_images")),
                ("slug", models.SlugField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_that_last_updated",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_that_last_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="blog.category",
                    ),
                ),
                (
                    "comments",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.comment",
                    ),
                ),
                (
                    "table_of_content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blog.tableofcontent",
                    ),
                ),
                ("tags", models.ManyToManyField(to="blog.tag")),
            ],
        ),
    ]
