from rest_framework import serializers
from .models import Entrepreneur

class EntrepreneurSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Entrepreneur
        fields = '__all__'

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        entrepreneur = Entrepreneur(**validated_data)
        entrepreneur.save()
        return entrepreneur
