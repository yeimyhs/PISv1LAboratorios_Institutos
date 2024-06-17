from rest_framework.viewsets import ModelViewSet
from sileii.serializers import ConvenioSerializer, DisciplinasSerializer, DocumentosSerializer, Entity3Serializer, Entity5Serializer, Entity6Serializer, EquipoSerializer, EventoGaleriaSerializer, FuncionSerializer, InstitutoSerializer, LaboratorioSerializer, LineaInvestigacionSerializer, PoiSerializer, ProyectoSerializer, PublicacionSerializer, RolInstSerializer, RolLabSerializer, RolUniSerializer, ServicioSerializer, SolicitudSerializer, SolicitudInstSerializer, SolicitudLabSerializer, SolitudUnidadSerializer, UnidadSerializer, UsersSerializer
from sileii.models import Convenio, Disciplinas, Documentos, Entity3, Entity5, Entity6, Equipo, EventoGaleria, Funcion, Instituto, Laboratorio, LineaInvestigacion, Poi, Proyecto, Publicacion, RolInst, RolLab, RolUni, Servicio, Solicitud, SolicitudInst, SolicitudLab, SolitudUnidad, Unidad, Users


class ConvenioViewSet(ModelViewSet):
    queryset = Convenio.objects.order_by('pk')
    serializer_class = ConvenioSerializer


class DisciplinasViewSet(ModelViewSet):
    queryset = Disciplinas.objects.order_by('pk')
    serializer_class = DisciplinasSerializer


class DocumentosViewSet(ModelViewSet):
    queryset = Documentos.objects.order_by('pk')
    serializer_class = DocumentosSerializer


class Entity3ViewSet(ModelViewSet):
    queryset = Entity3.objects.order_by('pk')
    serializer_class = Entity3Serializer


class Entity5ViewSet(ModelViewSet):
    queryset = Entity5.objects.order_by('pk')
    serializer_class = Entity5Serializer


class Entity6ViewSet(ModelViewSet):
    queryset = Entity6.objects.order_by('pk')
    serializer_class = Entity6Serializer


class EquipoViewSet(ModelViewSet):
    queryset = Equipo.objects.order_by('pk')
    serializer_class = EquipoSerializer


class EventoGaleriaViewSet(ModelViewSet):
    queryset = EventoGaleria.objects.order_by('pk')
    serializer_class = EventoGaleriaSerializer


class FuncionViewSet(ModelViewSet):
    queryset = Funcion.objects.order_by('pk')
    serializer_class = FuncionSerializer


class InstitutoViewSet(ModelViewSet):
    queryset = Instituto.objects.order_by('pk')
    serializer_class = InstitutoSerializer


class LaboratorioViewSet(ModelViewSet):
    queryset = Laboratorio.objects.order_by('pk')
    serializer_class = LaboratorioSerializer


class LineaInvestigacionViewSet(ModelViewSet):
    queryset = LineaInvestigacion.objects.order_by('pk')
    serializer_class = LineaInvestigacionSerializer


class PoiViewSet(ModelViewSet):
    queryset = Poi.objects.order_by('pk')
    serializer_class = PoiSerializer


class ProyectoViewSet(ModelViewSet):
    queryset = Proyecto.objects.order_by('pk')
    serializer_class = ProyectoSerializer


class PublicacionViewSet(ModelViewSet):
    queryset = Publicacion.objects.order_by('pk')
    serializer_class = PublicacionSerializer


class RolInstViewSet(ModelViewSet):
    queryset = RolInst.objects.order_by('pk')
    serializer_class = RolInstSerializer


class RolLabViewSet(ModelViewSet):
    queryset = RolLab.objects.order_by('pk')
    serializer_class = RolLabSerializer


class RolUniViewSet(ModelViewSet):
    queryset = RolUni.objects.order_by('pk')
    serializer_class = RolUniSerializer


class ServicioViewSet(ModelViewSet):
    queryset = Servicio.objects.order_by('pk')
    serializer_class = ServicioSerializer


class SolicitudViewSet(ModelViewSet):
    queryset = Solicitud.objects.order_by('pk')
    serializer_class = SolicitudSerializer


class SolicitudInstViewSet(ModelViewSet):
    queryset = SolicitudInst.objects.order_by('pk')
    serializer_class = SolicitudInstSerializer


class SolicitudLabViewSet(ModelViewSet):
    queryset = SolicitudLab.objects.order_by('pk')
    serializer_class = SolicitudLabSerializer


class SolitudUnidadViewSet(ModelViewSet):
    queryset = SolitudUnidad.objects.order_by('pk')
    serializer_class = SolitudUnidadSerializer


class UnidadViewSet(ModelViewSet):
    queryset = Unidad.objects.order_by('pk')
    serializer_class = UnidadSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.order_by('pk')
    serializer_class = UsersSerializer
