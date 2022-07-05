# Generated by Django 4.0.5 on 2022-07-04 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academiapp', '0009_mascota_email_responsable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='apellido_Responsable',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='dni_Responsable',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='email_Responsable',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='nombre_Responsable',
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='descripcion',
            field=models.TextField(max_length=100),
        ),
        migrations.CreateModel(
            name='Clienta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_Responsable', models.CharField(max_length=20)),
                ('nombre_Responsable', models.CharField(max_length=20)),
                ('apellido_Responsable', models.CharField(max_length=20)),
                ('email_Responsable', models.EmailField(default='name@yahoo.com', max_length=30)),
                ('mascota_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academiapp.mascota')),
            ],
        ),
    ]