from .models import Task, TimeHorizon, TaskStatus
from rest_framework import serializers


class DurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeHorizon
        fields = [
            "id",
            "duration",
        ]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = [
            "id",
            "task_status",
        ]


class TaskSerializer(serializers.ModelSerializer):
    # duration_lvl = DurationSerializer(read_only=True)
    # duration_lvl = serializers.StringRelatedField()
    # duration_lvl = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Task
        fields = [
            "id",
            "task",
            "status",
            "comment",
            "duration_lvl",
            "created_at",
            "updated_at",
            "deadline",
        ]
