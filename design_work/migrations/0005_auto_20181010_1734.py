# Generated by Django 2.0.8 on 2018-10-10 17:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('design_work', '0004_auto_20181004_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designworkpage',
            name='body',
            field=wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock(label='Изображение', required=True)), ('caption', wagtail.core.blocks.CharBlock(label='Описание', required=False)), ('attribution', wagtail.core.blocks.CharBlock(label='др. аттрибуты', required=False))], blank=True, null=True, verbose_name='Page body'),
        ),
        migrations.AlterField(
            model_name='designworkpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Основное изображение'),
        ),
    ]