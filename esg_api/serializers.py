from rest_framework import serializers
from .models import Company, ESGData

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ESGDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESGData
        fields = '__all__'
