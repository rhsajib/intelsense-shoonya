# Generated by Django 3.2.14 on 2023-04-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataset", "0037_translationpair_domain"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversation",
            name="conversation_quality_status",
            field=models.CharField(
                choices=[
                    ("Unchecked", "Unchecked"),
                    ("Clean", "Clean"),
                    ("Profane", "Profane"),
                    ("Difficult vocabulary", "Difficult vocabulary"),
                    ("Ambiguous sentence", "Ambiguous sentence"),
                    ("Context incomplete", "Context incomplete"),
                    ("Corrupt", "Corrupt"),
                ],
                default="Unchecked",
                help_text="Quality of the Sentence",
                max_length=32,
                verbose_name="quality_status",
            ),
        ),
        migrations.AddField(
            model_name="conversation",
            name="unverified_conversation_json",
            field=models.JSONField(
                blank=True,
                help_text="Details of the unverified conversation",
                null=True,
                verbose_name="unverified_conversation_details",
            ),
        ),
        migrations.AlterField(
            model_name="sentencetext",
            name="domain",
            field=models.CharField(
                choices=[
                    ("None", "None"),
                    ("Business", "Business"),
                    ("Culture", "Culture"),
                    ("General", "General"),
                    ("News", "News"),
                    ("Education", "Education"),
                    ("Legal", "Legal"),
                    ("Government-Press-Release", "Government-Press-Release"),
                    ("Healthcare", "Healthcare"),
                    ("Agriculture", "Agriculture"),
                    ("Automobile", "Automobile"),
                    ("Tourism", "Tourism"),
                    ("Financial", "Financial"),
                    ("Movies", "Movies"),
                    ("Subtitles", "Subtitles"),
                    ("Sports", "Sports"),
                    ("Technology", "Technology"),
                    ("Lifestyle", "Lifestyle"),
                    ("Entertainment", "Entertainment"),
                    ("Parliamentary", "Parliamentary"),
                    ("Art-and-Culture", "Art-and-Culture"),
                    ("Economy", "Economy"),
                    ("History", "History"),
                    ("Philosophy", "Philosophy"),
                    ("Religion", "Religion"),
                    ("National-Security-and-Defence", "National-Security-and-Defence"),
                    ("Literature", "Literature"),
                    ("Geography", "Geography"),
                ],
                default="None",
                help_text="Domain of the Sentence",
                max_length=1024,
                verbose_name="domain",
            ),
        ),
        migrations.AlterField(
            model_name="translationpair",
            name="domain",
            field=models.CharField(
                choices=[
                    ("None", "None"),
                    ("Business", "Business"),
                    ("Culture", "Culture"),
                    ("General", "General"),
                    ("News", "News"),
                    ("Education", "Education"),
                    ("Legal", "Legal"),
                    ("Government-Press-Release", "Government-Press-Release"),
                    ("Healthcare", "Healthcare"),
                    ("Agriculture", "Agriculture"),
                    ("Automobile", "Automobile"),
                    ("Tourism", "Tourism"),
                    ("Financial", "Financial"),
                    ("Movies", "Movies"),
                    ("Subtitles", "Subtitles"),
                    ("Sports", "Sports"),
                    ("Technology", "Technology"),
                    ("Lifestyle", "Lifestyle"),
                    ("Entertainment", "Entertainment"),
                    ("Parliamentary", "Parliamentary"),
                    ("Art-and-Culture", "Art-and-Culture"),
                    ("Economy", "Economy"),
                    ("History", "History"),
                    ("Philosophy", "Philosophy"),
                    ("Religion", "Religion"),
                    ("National-Security-and-Defence", "National-Security-and-Defence"),
                    ("Literature", "Literature"),
                    ("Geography", "Geography"),
                ],
                default="None",
                help_text="Domain of the Sentence",
                max_length=1024,
                verbose_name="domain",
            ),
        ),
    ]
