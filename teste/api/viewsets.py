from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *

class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()
    
    
class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    