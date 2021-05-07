from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import *
from .serializers import *
from django_filters import rest_framework as filters


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all().order_by('nome')  

    def post(self, request, *args, **kwargs):
        data = request.data
        
        nome = data["nome"]
        
        if (nome == ''):
            raise ParseError(detail="Favor inserir um nome", code=400)
        
        obj_empresa = Empresa.objects.create(nome=nome)
        obj_empresa.save()
        
        serializer = EmpresaSerializer(obj_empresa)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all().order_by('username')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['username']

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data["username"]
        
        if (username == ''):
            raise ParseError(detail="Favor inserir um nome", code=400)
        
        if Usuario.objects.filter(username=username).exists():
            return Response({"detail":"Usuário existente, escolha outro nome"}, status=status.HTTP_409_CONFLICT)
                
        obj_usuario = Usuario.objects.create(username=username)
        obj_usuario.save()
        
        if ("empresas" in data):
            for empresa in data["empresas"]:
                empresa_id = int(empresa["id"])
                try:
                    obj_empresa = Empresa.objects.get(id=empresa_id)
                except:
                    raise NotFound(
                        detail=f"Empresa {empresa_id} não encontrada", code=404)
                obj_usuario.empresas.add(obj_empresa)

        serializer = UsuarioSerializer(obj_usuario)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
