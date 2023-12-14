# Generated by Django 3.1.14 on 2022-09-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0029_auto_20220722_1216"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="users",
            new_name="annotators",
        ),
        migrations.AlterField(
            model_name="project",
            name="project_type",
            field=models.CharField(
                choices=[
                    ("MonolingualTranslation", "MonolingualTranslation"),
                    ("TranslationEditing", "TranslationEditing"),
                    (
                        "SemanticTextualSimilarity_Scale5",
                        "SemanticTextualSimilarity_Scale5",
                    ),
                    ("ContextualTranslationEditing", "ContextualTranslationEditing"),
                    ("OCRAnnotation", "OCRAnnotation"),
                    ("MonolingualCollection", "MonolingualCollection"),
                    ("SentenceSplitting", "SentenceSplitting"),
                    (
                        "ContextualSentenceVerification",
                        "ContextualSentenceVerification",
                    ),
                    ("ConversationTranslation", "ConversationTranslation"),
                ],
                help_text="Project Type indicating the annotation task",
                max_length=100,
            ),
        ),
    ]