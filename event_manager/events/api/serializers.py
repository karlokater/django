""" 
Ein Serializer wandelt eine Python-Datenstruktur in JSON um und 
eine JSON-Struktur in ein Python Objekt.

Der ModelSerializer serializiert uns Django-Model
"""

from rest_framework.serializers import ModelSerializer, StringRelatedField
from events.models import Category, Event, Tag


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    author = StringRelatedField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
