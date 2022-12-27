from rest_framework import serializers

from .models import Character


class CharactersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Character
        fields = ('__all__')
