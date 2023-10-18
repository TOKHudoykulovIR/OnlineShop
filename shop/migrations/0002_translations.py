# Generated by Django 4.2.6 on 2023-10-18 10:52

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryTranslation",
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
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "category Translation",
                "db_table": "shop_category_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.RemoveIndex(
            model_name="category",
            name="shop_catego_name_289c7e_idx",
        ),
        migrations.RemoveField(
            model_name="category",
            name="name",
        ),
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
        migrations.AddField(
            model_name="categorytranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="shop.category",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="categorytranslation",
            unique_together={("language_code", "master")},
        ),
    ]
