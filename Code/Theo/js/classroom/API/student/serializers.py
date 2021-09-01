from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'cohort',
            'fav_topic',
            'fav_teacher',
            'capstone',
            'id'
        )
        model = Student