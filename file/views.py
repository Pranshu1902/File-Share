from rest_framework import serializers, viewsets
from file.models import FileShare, User
from rest_framework.decorators import action

# Create your views here.
class FileShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileShare
        fields = ('sender', 'receiver', 'file')

class FileShareViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    serializer_class = FileShareSerializer

# User model viewset and serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("__all__")

class UserViewSet(viewsets.GenericViewSet, viewsets.ViewSet):
    serializer_class = UserSerializer
