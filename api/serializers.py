from rest_framework import serializers
from .models import *

class EmpresaSerializer(serializers.ModelSerializer):
    usuarios = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Empresa
        fields = ['nome', 'usuarios']
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        depth = 1