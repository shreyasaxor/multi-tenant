from rest_framework import serializers

from quickstart.models import Education


class EducationSerializer(serializers.Serializer):
    """This is the serializer used for logging in user"""


    class Meta:
        model = Education
        feilds = '__all__'