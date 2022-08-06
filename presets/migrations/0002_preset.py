# Generated by Django 4.1 on 2022-08-06 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('fifth_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fifth_art', to='presets.artifact')),
                ('first_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_art', to='presets.artifact')),
                ('fourth_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fourth_art', to='presets.artifact')),
                ('second_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_art', to='presets.artifact')),
                ('third_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_art', to='presets.artifact')),
            ],
        ),
    ]