from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r"tareas", TaskViewSet, basename="tarea")

urlpatterns = router.urls