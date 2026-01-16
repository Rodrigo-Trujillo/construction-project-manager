from rest_framework import viewsets, filters
from .models import Project, Activity, Cost
from .serializers import ProjectSerializer, ActivitySerializer, CostSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

    # búsqueda por nombre, cliente o ubicación
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'client', 'location']

    # ordenar por fechas o creación
    ordering_fields = ['start_date', 'end_date', 'created_at']
    ordering = ['-created_at']  # por defecto los más recientes primero


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class CostViewSet(viewsets.ModelViewSet):
    queryset = Cost.objects.all()
    serializer_class = CostSerializer



