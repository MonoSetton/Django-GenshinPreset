from rest_framework.response import Response
from rest_framework.decorators import api_view
from updatedb.models import Character, Weapon, Artifact_set
from .serializers import CharacterSerializer, WeaponSerializer, ArtifactSetSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Characters': '/character-list/',
        'Weapons': '/weapon-list/',
        'Artifact Sets': '/artifact-set-list/'
    }
    return Response(api_urls)


@api_view(['GET'])
def character_list(request):
    characters = Character.objects.all().order_by('name')
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def weapon_list(request):
    weapons = Weapon.objects.all().order_by('name')
    serializer = WeaponSerializer(weapons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def artifact_set_list(request):
    artifact_sets = Artifact_set.objects.all().order_by('name')
    serializer = ArtifactSetSerializer(artifact_sets, many=True)
    return Response(serializer.data)

