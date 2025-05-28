from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend_tasks.api_views import TaskViewSet,TaskFilterApiView

router = DefaultRouter()
router.register(r'frontend_tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('frontend_tasks/filter/', TaskFilterApiView.as_view(), name='task-filter'),
]
