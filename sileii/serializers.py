from rest_framework.serializers import ModelSerializer
from sileii.models import Convenio, Disciplinas, Documentos, Entity3, Entity5, Entity6, Equipo, EventoGaleria, Funcion, Instituto, Laboratorio, LineaInvestigacion, Poi, Proyecto, Publicacion, RolInst, RolLab, RolUni, Servicio, Solicitud, SolicitudInst, SolicitudLab, SolitudUnidad, Unidad, Users


class ConvenioSerializer(ModelSerializer):

    class Meta:
        model = Convenio
        fields = '__all__'


class DisciplinasSerializer(ModelSerializer):

    class Meta:
        model = Disciplinas
        fields = '__all__'


class DocumentosSerializer(ModelSerializer):

    class Meta:
        model = Documentos
        fields = '__all__'


class Entity3Serializer(ModelSerializer):

    class Meta:
        model = Entity3
        fields = '__all__'


class Entity5Serializer(ModelSerializer):

    class Meta:
        model = Entity5
        fields = '__all__'


class Entity6Serializer(ModelSerializer):

    class Meta:
        model = Entity6
        fields = '__all__'


class EquipoSerializer(ModelSerializer):

    class Meta:
        model = Equipo
        fields = '__all__'


class EventoGaleriaSerializer(ModelSerializer):

    class Meta:
        model = EventoGaleria
        fields = '__all__'


class FuncionSerializer(ModelSerializer):

    class Meta:
        model = Funcion
        fields = '__all__'


class InstitutoSerializer(ModelSerializer):

    class Meta:
        model = Instituto
        fields = '__all__'


class LaboratorioSerializer(ModelSerializer):

    class Meta:
        model = Laboratorio
        fields = '__all__'


class LineaInvestigacionSerializer(ModelSerializer):

    class Meta:
        model = LineaInvestigacion
        fields = '__all__'


class PoiSerializer(ModelSerializer):

    class Meta:
        model = Poi
        fields = '__all__'


class ProyectoSerializer(ModelSerializer):

    class Meta:
        model = Proyecto
        fields = '__all__'


class PublicacionSerializer(ModelSerializer):

    class Meta:
        model = Publicacion
        fields = '__all__'


class RolInstSerializer(ModelSerializer):

    class Meta:
        model = RolInst
        fields = '__all__'


class RolLabSerializer(ModelSerializer):

    class Meta:
        model = RolLab
        fields = '__all__'


class RolUniSerializer(ModelSerializer):

    class Meta:
        model = RolUni
        fields = '__all__'


class ServicioSerializer(ModelSerializer):

    class Meta:
        model = Servicio
        fields = '__all__'


class SolicitudSerializer(ModelSerializer):

    class Meta:
        model = Solicitud
        fields = '__all__'


class SolicitudInstSerializer(ModelSerializer):

    class Meta:
        model = SolicitudInst
        fields = '__all__'


class SolicitudLabSerializer(ModelSerializer):

    class Meta:
        model = SolicitudLab
        fields = '__all__'


class SolitudUnidadSerializer(ModelSerializer):

    class Meta:
        model = SolitudUnidad
        fields = '__all__'


class UnidadSerializer(ModelSerializer):

    class Meta:
        model = Unidad
        fields = '__all__'


class UsersSerializer(ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
