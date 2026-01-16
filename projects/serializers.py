from rest_framework import serializers
from .models import Project, Activity, Cost


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    costs = CostSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
