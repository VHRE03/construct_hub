from django.urls import include, path
from rest_framework import routers
from .views import TaskAssignmentViewSet

router = routers.DefaultRouter()
router.register(r'task-assignment', TaskAssignmentViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]
