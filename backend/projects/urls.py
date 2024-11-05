from django.urls import include, path
from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
