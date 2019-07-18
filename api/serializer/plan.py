from rest_framework import serializers
from api.models.plan import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan

        fields = ["pk", "name", "lower_percentage", "min_value", "upper_percentage"]
