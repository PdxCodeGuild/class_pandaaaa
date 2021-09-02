from rest_framework import serializers
from myapp import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'firstName',
            'lastName',
            'cohort',
            'favoriteTopic',
            'favoriteTeacher',
            'capstone',
        )
        model = models.Student
