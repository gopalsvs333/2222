from rest_framework import serializers
from .models import Student,Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta():
        model=Subject
        fields='__all__'
class StudentSerializer(serializers.ModelSerializer):
    # subjects = SubjectSerializer(read_only=True, many=True)
    class Meta():
        model = Student
        fields ='__all__'
