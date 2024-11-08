from django.urls import include, path
from rest_framework import routers
from .views import RoleViewSet

router = routers.DefaultRouter()
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
