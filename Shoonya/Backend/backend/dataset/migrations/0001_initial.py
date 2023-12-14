# Generated by Django 3.2.12 on 2022-03-03 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DatasetBase",
            fields=[
                (
                    "data_id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="data_id"
                    ),
                ),
                (
                    "metadata_json",
                    models.JSONField(
                        blank=True, null=True, verbose_name="metadata_json"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SentenceText",
            fields=[
                (
                    "datasetbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dataset.datasetbase",
                    ),
                ),
                (
                    "lang_id",
                    models.CharField(
                        choices=[
                            ("bn", "Bengali"),
                            ("gu", "Gujarati"),
                            ("en", "English"),
                            ("hi", "Hindi"),
                            ("kn", "Kannada"),
                            ("mr", "Marathi"),
                            ("ne", "Nepali"),
                            ("ne", "Odia"),
                            ("pa", "Punjabi"),
                            ("sa", "Sanskrit"),
                            ("ta", "Tamil"),
                            ("te", "Telugu"),
                        ],
                        max_length=100,
                        verbose_name="language_id",
                    ),
                ),
                ("text", models.TextField(verbose_name="text")),
                ("domain", models.CharField(max_length=1024, verbose_name="domain")),
                ("is_profane", models.BooleanField(null=True)),
            ],
            bases=("dataset.datasetbase",),
        ),
        migrations.CreateModel(
            name="TranslationPair",
            fields=[
                (
                    "datasetbase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dataset.datasetbase",
                    ),
                ),
                (
                    "input_lang_id",
                    models.CharField(
                        choices=[
                            ("bn", "Bengali"),
                            ("gu", "Gujarati"),
                            ("en", "English"),
                            ("hi", "Hindi"),
                            ("kn", "Kannada"),
                            ("mr", "Marathi"),
                            ("ne", "Nepali"),
                            ("ne", "Odia"),
                            ("pa", "Punjabi"),
                            ("sa", "Sanskrit"),
                            ("ta", "Tamil"),
                            ("te", "Telugu"),
                        ],
                        max_length=100,
                        verbose_name="input_language_id",
                    ),
                ),
                (
                    "output_lang_id",
                    models.CharField(
                        choices=[
                            ("bn", "Bengali"),
                            ("gu", "Gujarati"),
                            ("en", "English"),
                            ("hi", "Hindi"),
                            ("kn", "Kannada"),
                            ("mr", "Marathi"),
                            ("ne", "Nepali"),
                            ("ne", "Odia"),
                            ("pa", "Punjabi"),
                            ("sa", "Sanskrit"),
                            ("ta", "Tamil"),
                            ("te", "Telugu"),
                        ],
                        max_length=100,
                        verbose_name="output_language_id",
                    ),
                ),
                ("input_text", models.TextField(verbose_name="input_text")),
                ("output_text", models.TextField(verbose_name="output_text")),
                (
                    "machine_translation",
                    models.TextField(null=True, verbose_name="machine_translation"),
                ),
                (
                    "labse_score",
                    models.DecimalField(decimal_places=2, max_digits=4, null=True),
                ),
                (
                    "rating",
                    models.IntegerField(null=True, verbose_name="translation_rating"),
                ),
            ],
            bases=("dataset.datasetbase",),
        ),
        migrations.CreateModel(
            name="DatasetInstance",
            fields=[
                (
                    "instance_id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="dataset_instance_id",
                    ),
                ),
                (
                    "parent_instance_id",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="parent_instance_id"
                    ),
                ),
                (
                    "instance_name",
                    models.CharField(
                        max_length=1024, verbose_name="dataset_instance_name"
                    ),
                ),
                (
                    "instance_description",
                    models.TextField(
                        null=True, verbose_name="dataset_instance_description"
                    ),
                ),
                (
                    "organisation_id",
                    models.IntegerField(null=True, verbose_name="organisation_id"),
                ),
                (
                    "workspace_id",
                    models.IntegerField(null=True, verbose_name="workspace_id"),
                ),
                (
                    "dataset_type",
                    models.CharField(
                        choices=[
                            ("sentence_text", "SentenceText"),
                            ("translation_pair", "TranslationPair"),
                        ],
                        max_length=100,
                        verbose_name="dataset_type",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        related_name="dataset_users", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "db_table": "dataset_instance",
            },
        ),
        migrations.AddField(
            model_name="datasetbase",
            name="instance_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="dataset.datasetinstance",
            ),
        ),
        migrations.AddIndex(
            model_name="datasetinstance",
            index=models.Index(
                fields=["instance_id"], name="dataset_ins_instanc_12aa42_idx"
            ),
        ),
    ]