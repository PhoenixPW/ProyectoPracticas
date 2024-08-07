# Generated by Django 5.0.2 on 2024-08-08 18:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clase2',
            fields=[
                ('nrc', models.BigIntegerField(primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=10)),
                ('seccion', models.CharField(max_length=4)),
                ('nombreMateria', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id_criterio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('plan', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('FINALIZADO', 'FINALIZADO')], max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('age', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('matricula', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contrasena', models.CharField(blank=True, max_length=100)),
                ('id_usuario', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ClaseCriterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('ponderacion', models.FloatField()),
                ('id_clase', models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.clase2')),
                ('id_criterio', models.ForeignKey(db_constraint=False, default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.criterio')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('fecha', models.DateField()),
                ('estado', models.CharField(choices=[('REGISTRADA', 'REGISTRADA'), ('PENDIENTE', 'PENDIENTE')], max_length=50)),
                ('tipo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.clasecriterio')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('matricula', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.alumno')),
                ('id_entrega', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.entrega')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('ACTIVA', 'ACTIVA'), ('PENDIENTE', 'PENDIENTE'), ('BAJA', 'BAJA'), ('ARCHIVADA', 'ARCHIVADA')], max_length=50)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.alumno')),
                ('clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.clase2')),
            ],
        ),
        migrations.AddField(
            model_name='clase2',
            name='id_periodo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.periodo'),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('correo', models.CharField(blank=True, max_length=100)),
                ('contrasena', models.CharField(blank=True, max_length=100)),
                ('token', models.CharField(blank=True, max_length=50)),
                ('id_usuario', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='clase2',
            name='id_profesor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='api.profesor'),
        ),
    ]
