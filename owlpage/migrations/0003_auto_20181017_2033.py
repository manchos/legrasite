# Generated by Django 2.0.8 on 2018-10-17 20:33

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('owlpage', '0002_auto_20181017_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owlpage',
            name='body',
            field=wagtail.core.fields.StreamField([('owl_paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))], blank=True, null=True, verbose_name='Параграф-описание'),
        ),
    ]
