from django.urls import include, path
from rest_framework import routers
from .views import WorkerViewSet

router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
