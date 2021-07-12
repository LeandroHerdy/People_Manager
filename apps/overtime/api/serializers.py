from rest_framework import serializers

from apps.overtime.models import Overtime


class OvertimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overtime
        fields = ['remark', 'employee', 'hour']
