from django.contrib import admin
from .models import Project, Activity, Cost


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'start_date')
    search_fields = ('name', 'client')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'status', 'progress')
    list_filter = ('status', 'project')
    search_fields = ('name', 'project__name')


@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('project', 'category', 'budgeted_amount', 'actual_amount')
    list_filter = ('project', 'category')
    search_fields = ('project__name', 'category')



