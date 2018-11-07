# Generated by Django 2.0.8 on 2018-10-22 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('design_work', '0012_auto_20181019_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Вид дизанерских работ',
                'verbose_name_plural': 'Виды дизанерских работ',
            },
        ),
        migrations.AlterModelOptions(
            name='designworkindexpage',
            options={'verbose_name': 'Дизайн-работы с таблицей изображений', 'verbose_name_plural': 'Перечень работ с таблицей изображений'},
        ),
        migrations.AddField(
            model_name='designworkpage',
            name='design_kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='design_work.DesignKind', verbose_name='Вид дизанерских работ'),
        ),
    ]