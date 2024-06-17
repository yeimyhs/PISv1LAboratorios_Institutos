from rest_framework.routers import SimpleRouter
from sileii import views


router = SimpleRouter()

router.register(r'convenio', views.ConvenioViewSet)
router.register(r'disciplinas', views.DisciplinasViewSet)
router.register(r'documentos', views.DocumentosViewSet)
router.register(r'entity3', views.Entity3ViewSet)
router.register(r'entity5', views.Entity5ViewSet)
router.register(r'entity6', views.Entity6ViewSet)
router.register(r'equipo', views.EquipoViewSet)
router.register(r'eventogaleria', views.EventoGaleriaViewSet)
router.register(r'funcion', views.FuncionViewSet)
router.register(r'instituto', views.InstitutoViewSet)
router.register(r'laboratorio', views.LaboratorioViewSet)
router.register(r'lineainvestigacion', views.LineaInvestigacionViewSet)
router.register(r'poi', views.PoiViewSet)
router.register(r'proyecto', views.ProyectoViewSet)
router.register(r'publicacion', views.PublicacionViewSet)
router.register(r'rolinst', views.RolInstViewSet)
router.register(r'rollab', views.RolLabViewSet)
router.register(r'roluni', views.RolUniViewSet)
router.register(r'servicio', views.ServicioViewSet)
router.register(r'solicitud', views.SolicitudViewSet)
router.register(r'solicitudinst', views.SolicitudInstViewSet)
router.register(r'solicitudlab', views.SolicitudLabViewSet)
router.register(r'solitudunidad', views.SolitudUnidadViewSet)
router.register(r'unidad', views.UnidadViewSet)
router.register(r'users', views.UsersViewSet)

urlpatterns = router.urls
