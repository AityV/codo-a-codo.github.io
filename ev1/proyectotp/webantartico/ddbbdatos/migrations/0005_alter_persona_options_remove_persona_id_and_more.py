# Generated by Django 5.0 on 2023-12-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddbbdatos', '0004_alter_persona_telefono'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['IdPersona']},
        ),
        migrations.RemoveField(
            model_name='persona',
            name='id',
        ),
        migrations.AlterField(
            model_name='persona',
            name='IdPersona',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
