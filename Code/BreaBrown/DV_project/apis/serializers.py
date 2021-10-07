from rest_framework import serializers
from studentsapp import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Students