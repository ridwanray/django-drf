from rest_framework import serializers

from .models import Job


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(allow_blank=False)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ["title", "company_name", "employment_type", "description"]
