# Generated by Django 2.0.8 on 2018-10-18 11:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('design_work', '0007_auto_20181010_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designworkpage',
            name='image',
        ),
        migrations.AlterField(
            model_name='designworkpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение', required=True)), ('caption', wagtail.core.blocks.CharBlock(label='Описание', required=False)), ('attribution', wagtail.core.blocks.CharBlock(label='др. аттрибуты', required=False))]))], verbose_name='Дополнительные изображения'),
        ),
    ]
