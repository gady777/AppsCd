from rest_framework import serializers
from register.models import Entrepreneur

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            entrepreneur = Entrepreneur.objects.get(email=email)
        except Entrepreneur.DoesNotExist:
            raise serializers.ValidationError("Les informations de connexion ne sont pas valides.")

        if entrepreneur.check_password(password):
            data['user'] = entrepreneur
        else:
            raise serializers.ValidationError("Les informations de connexion ne sont pas valides.")

        return data
