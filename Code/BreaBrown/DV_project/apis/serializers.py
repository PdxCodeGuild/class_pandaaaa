from rest_framework import serializers
from studentsapp import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'fname',
            'lname',
            'Cohort',
            'fav_topic',
            'fav_teacher',
            'Capstone',
        )
        model = models.Students