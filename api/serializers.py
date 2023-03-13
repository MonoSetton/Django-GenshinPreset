from rest_framework import serializers
from updatedb.models import Character, Weapon, Artifact_set


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'weapon', 'vision']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['name', 'type', 'atk', 'stat', 'ability']


class ArtifactSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact_set
        fields = ['name', 'piece_2', 'piece_4']