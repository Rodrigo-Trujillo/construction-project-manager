from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet, ActivityViewSet, CostViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'costs', CostViewSet, basename='cost')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

