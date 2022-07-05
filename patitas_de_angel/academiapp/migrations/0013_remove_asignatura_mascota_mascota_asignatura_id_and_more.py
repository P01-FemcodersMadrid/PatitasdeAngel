# Generated by Django 4.0.5 on 2022-07-04 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academiapp', '0012_clienta_movil_responsable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignatura',
            name='mascota',
        ),
        migrations.AddField(
            model_name='mascota',
            name='asignatura_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academiapp.asignatura'),
        ),
        migrations.DeleteModel(
            name='Entrenadora',
        ),
    ]