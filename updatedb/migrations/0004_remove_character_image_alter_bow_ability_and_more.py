# Generated by Django 4.1 on 2022-08-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updatedb', '0003_artifact_set_delete_artifact_sets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='image',
        ),
        migrations.AlterField(
            model_name='bow',
            name='ability',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='catalyst',
            name='ability',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='claymore',
            name='ability',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='polearm',
            name='ability',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sword',
            name='ability',
            field=models.TextField(),
        ),
    ]