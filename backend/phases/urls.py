from django.urls import include, path
from rest_framework import routers
from .views import PhaseViewSet

router = routers.DefaultRouter()
router.register(r'phases', PhaseViewSet)
urlpatterns = [
    path('v1/', include(router.urls))
]
