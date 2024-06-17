# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Convenio(models.Model):
    convenio_id = models.BigAutoField(primary_key=True)
    instituto = models.ForeignKey('Instituto', models.DO_NOTHING)
    entidad = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    objetivo = models.TextField()
    detalles = models.TextField()
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Convenio'

class Disciplinas(models.Model):
    disciplina_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Disciplinas'

class Documentos(models.Model):
    documento_id = models.BigAutoField(primary_key=True)
    registro = models.ForeignKey('Laboratorio', models.DO_NOTHING)
    nombre_documento = models.CharField(max_length=255)
    archivo_documento = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Documentos'

class Entity3(models.Model):
    lininvest = models.OneToOneField('LineaInvestigacion', models.DO_NOTHING, db_column='linInvest_id', primary_key=True)  # Field name made lowercase. The composite primary key (linInvest_id, proyecto_id) found, that is not supported. The first column is selected.
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING)
    class Meta:
        db_table = 'Entity3'
        unique_together = (('lininvest', 'proyecto'),)

class Entity5(models.Model):
    solicitud = models.OneToOneField('Solicitud', models.DO_NOTHING, primary_key=True)  # The composite primary key (solicitud_id, equipo_id) found, that is not supported. The first column is selected.
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING)
    class Meta:
        db_table = 'Entity5'
        unique_together = (('solicitud', 'equipo'),)

class Entity6(models.Model):
    registro = models.OneToOneField('Laboratorio', models.DO_NOTHING, primary_key=True)  # The composite primary key (registro_id, disciplina_id) found, that is not supported. The first column is selected.
    disciplina = models.ForeignKey(Disciplinas, models.DO_NOTHING)
    class Meta:
        db_table = 'Entity6'
        unique_together = (('registro', 'disciplina'),)

class Equipo(models.Model):
    equipo_id = models.BigAutoField(primary_key=True)
    registro = models.ForeignKey('Laboratorio', models.DO_NOTHING)
    nombre_imagen = models.CharField(max_length=255, blank=True, null=True)
    imagen_equipo = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    marca_modelo = models.CharField(max_length=255)
    fecha_adquisicion = models.DateTimeField()
    proveedor = models.CharField(max_length=100)
    contacto_proveedor = models.CharField(max_length=100)
    codigo_patrimonio = models.CharField(max_length=50)
    accesorio = models.CharField(max_length=255)
    insumos = models.TextField()
    descripcion = models.TextField()
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Equipo'

class EventoGaleria(models.Model):
    galeria_id = models.BigAutoField(primary_key=True)
    registro = models.ForeignKey('Laboratorio', models.DO_NOTHING)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Evento_galeria'

class Funcion(models.Model):
    funcion_id = models.BigAutoField(primary_key=True)
    instituto = models.ForeignKey('Instituto', models.DO_NOTHING)
    funcion = models.CharField(max_length=255)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Funcion'

class Instituto(models.Model):
    instituto_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    ubicacion = models.TextField(blank=True, null=True)
    comite_directivo = models.TextField(blank=True, null=True)
    contacto = models.TextField(blank=True, null=True)
    nombre_imagen = models.CharField(max_length=255, blank=True, null=True)
    imagen_instituto = models.CharField(max_length=255, blank=True, null=True)
    url_instituto = models.TextField(blank=True, null=True)
    url_facebook = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Instituto'

class Laboratorio(models.Model):
    registro_id = models.BigAutoField(primary_key=True)
    area = models.CharField(max_length=255)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    servicios = models.JSONField(blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Laboratorio'

class LineaInvestigacion(models.Model):
    nombre = models.CharField(max_length=255)
    lininvest_id = models.BigIntegerField(db_column='linInvest_id', primary_key=True)  # Field name made lowercase.
    detalle = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'Linea_Investigacion'

class Poi(models.Model):
    poi_id = models.BigAutoField(primary_key=True)
    instituto = models.ForeignKey(Instituto, models.DO_NOTHING)
    ano = models.IntegerField()
    nombre_poi = models.CharField(max_length=255, blank=True, null=True)
    archivo_poi = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Poi'

class Proyecto(models.Model):
    proyecto_id = models.BigAutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=255)
    investigador_principal = models.CharField(max_length=255)
    coinvestigadores = models.JSONField()
    nombre_imagen = models.CharField(max_length=255, blank=True, null=True)
    imagen_referencial = models.CharField(max_length=255, blank=True, null=True)
    etapa = models.CharField(max_length=255, blank=True, null=True)
    duracion = models.CharField(max_length=255, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    doi = models.CharField(max_length=255)
    resumen = models.TextField()
    iba = models.CharField(max_length=25)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Proyecto'

class Publicacion(models.Model):
    publicacion_id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    link = models.TextField()
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        db_table = 'Publicacion'

class RolInst(models.Model):
    instituto = models.OneToOneField(Instituto, models.DO_NOTHING, primary_key=True)  # The composite primary key (instituto_id, usuario_id) found, that is not supported. The first column is selected.
    usuario = models.ForeignKey('Users', models.DO_NOTHING)
    tipo_rol = models.SmallIntegerField()
    class Meta:
        db_table = 'Rol_Inst'
        unique_together = (('instituto', 'usuario'),)

class RolLab(models.Model):
    usuario = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (usuario_id, registro_id) found, that is not supported. The first column is selected.
    registro = models.ForeignKey(Laboratorio, models.DO_NOTHING)
    tipo_rol = models.SmallIntegerField()
    class Meta:
        db_table = 'Rol_Lab'
        unique_together = (('usuario', 'registro'),)

class RolUni(models.Model):
    unidad = models.OneToOneField('Unidad', models.DO_NOTHING, primary_key=True)  # The composite primary key (unidad_id, usuario_id) found, that is not supported. The first column is selected.
    usuario = models.ForeignKey('Users', models.DO_NOTHING)
    tipo_rol = models.SmallIntegerField()
    class Meta:
        db_table = 'Rol_Uni'
        unique_together = (('unidad', 'usuario'),)

class Servicio(models.Model):
    servicio_id = models.BigAutoField(primary_key=True)
    instituto = models.ForeignKey(Instituto, models.DO_NOTHING)
    nombre = models.CharField(max_length=255)
    materiales = models.FloatField()
    mano_obra = models.FloatField()
    ci_mano_obra = models.FloatField()
    ci_deprec_equi = models.FloatField()
    ci_deprec_edif = models.FloatField()
    ci_util_limp = models.FloatField()
    ci_util_aseo = models.FloatField()
    ci_mantto = models.FloatField()
    ci_servicios = models.FloatField()
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Servicio'

class Solicitud(models.Model):
    solicitud_id = models.BigAutoField(primary_key=True)
    fecha_solicitud = models.DateField()
    detalle = models.TextField()
    oficio = models.TextField()
    etapa = models.CharField(max_length=255)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        db_table = 'Solicitud'

class SolicitudInst(models.Model):
    instituto = models.OneToOneField(Instituto, models.DO_NOTHING, primary_key=True)  # The composite primary key (instituto_id, proyecto_id) found, that is not supported. The first column is selected.
    proyecto = models.ForeignKey(Proyecto, models.DO_NOTHING)
    state = models.SmallIntegerField()
    created_at = models.DateTimeField()
    field_updated_at = models.DateTimeField(db_column='\x7fupdated_at')  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    solicitud_estado = models.SmallIntegerField()
    class Meta:
        db_table = 'Solicitud_Inst'
        unique_together = (('instituto', 'proyecto'),)

class SolicitudLab(models.Model):
    proyecto = models.OneToOneField(Proyecto, models.DO_NOTHING, primary_key=True)  # The composite primary key (proyecto_id, registro_id) found, that is not supported. The first column is selected.
    registro = models.ForeignKey(Laboratorio, models.DO_NOTHING)
    state = models.SmallIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    solicitud_estado = models.SmallIntegerField()
    class Meta:
        db_table = 'Solicitud_Lab'
        unique_together = (('proyecto', 'registro'),)

class SolitudUnidad(models.Model):
    proyecto = models.OneToOneField(Proyecto, models.DO_NOTHING, primary_key=True)  # The composite primary key (proyecto_id, unidad_id) found, that is not supported. The first column is selected.
    unidad = models.ForeignKey('Unidad', models.DO_NOTHING)
    state = models.SmallIntegerField()
    updated_at = models.DateTimeField()
    created_at_field = models.DateTimeField(db_column="created_at'")  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    solicitud_estado = models.SmallIntegerField()
    class Meta:
        db_table = 'Solitud_Unidad'
        unique_together = (('proyecto', 'unidad'),)

class Unidad(models.Model):
    unidad_id = models.BigAutoField(primary_key=True)
    director = models.CharField(max_length=250)
    facultad = models.CharField(max_length=255)
    class Meta:
        db_table = 'Unidad'

class Users(models.Model):
    usuario_id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45, blank=True, null=True)
    apellido_materno = models.CharField(max_length=45, blank=True, null=True)
    dni = models.CharField(unique=True, max_length=8)
    telefono = models.CharField(max_length=9, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=255)
    contrasena = models.CharField(max_length=255)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    fecha_eleccion = models.DateField(blank=True, null=True)
    fecha_culminacion = models.DateField(blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    regimen = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    email_verified_at = models.DateTimeField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'Users'

