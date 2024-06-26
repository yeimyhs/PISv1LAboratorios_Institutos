# Generated by Django 5.0.6 on 2024-06-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sileii', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenio',
            name='convenio_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='disciplinas',
            name='disciplina_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='documento_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='equipo_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='eventogaleria',
            name='galeria_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='funcion_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='registro_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='poi',
            name='poi_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='proyecto_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='publicacion_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='solicitud_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unidad',
            name='unidad_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='usuario_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
