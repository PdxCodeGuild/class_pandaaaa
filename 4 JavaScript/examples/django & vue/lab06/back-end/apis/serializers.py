from rest_framework import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'cohort',
            'favorite_teacher',
            'id'
        )
        model = models.Student