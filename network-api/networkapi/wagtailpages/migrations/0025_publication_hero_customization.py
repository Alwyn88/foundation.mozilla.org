# Generated by Django 3.2.13 on 2022-05-27 16:58

import django.db.models.deletion
import wagtail_color_panel.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtaildocs", "0012_uploadeddocument"),
        ("wagtailpages", "0024_researchauthorsindexpage_banner_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="publicationpage",
            name="displayed_hero_content",
            field=models.CharField(
                choices=[("image", "Image"), ("video", "Video")],
                default="image",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="download_button_icon",
            field=models.ForeignKey(
                blank=True,
                help_text="Custom Icon for download button, please use https://feathericons.com",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.document",
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="download_button_style",
            field=models.CharField(
                choices=[
                    ("primary", "Primary"),
                    ("secondary", "Secondary"),
                    ("tertiary", "Tertiary"),
                ],
                default="primary",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="hero_background_color",
            field=wagtail_color_panel.fields.ColorField(
                default="#ffffff",
                help_text="Please check your chosen background color with https://webaim.org/resources/contrastchecker/ to see if your text and background color pass accessibility standards. If your text is black enter #000000 in the Foreground Color box and #FFFFFF if your text is white. After you have selected your background color, please contact the design team for a design review!",
                max_length=7,
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="hero_layout",
            field=models.CharField(
                choices=[
                    ("full_screen", "Full Screen"),
                    ("image_left", "Image Left"),
                    ("image_right", "Image Right"),
                    ("static", "Static"),
                ],
                default="static",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="hero_text_color",
            field=models.CharField(
                choices=[("black", "Black"), ("white", "White")],
                default="black",
                help_text="For proper contrast, we recommend using “White” for dark background colors, and “Black” for light background colors.",
                max_length=25,
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="hero_video",
            field=models.CharField(
                blank=True,
                help_text='Log into Vimeo using 1Password and upload the desired video. Then select the video and click "Advanced", "Distribution", and "Video File Links". Copy and paste the link here.',
                max_length=500,
            ),
        ),
        migrations.AddField(
            model_name="publicationpage",
            name="show_authors",
            field=models.BooleanField(default=True, help_text="Display authors in the hero section"),
        ),
    ]
