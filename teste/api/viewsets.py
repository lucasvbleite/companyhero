from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import *
from .serializers import *
from django_filters import rest_framework as filters


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        if (data["nome"] == ''):
            raise ParseError(detail="Favor inserir um nome", code=400)
        obj_empresa = Empresa.objects.create(nome=data["nome"])
        obj_empresa.save()
        serializer = EmpresaSerializer(obj_empresa)

        return Response(serializer.data)


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['username']

    def post(self, request, *args, **kwargs):
        data = request.data
        if (data["username"] == ''):
            raise ParseError(detail="Favor inserir um nome", code=400)
        obj_usuario = Usuario.objects.create(username=data["username"])
        obj_usuario.save()

        for empresa in data["empresas"]:
            try:
                obj_empresa = Empresa.objects.get(id=empresa["id"])
            except:
                raise NotFound(
                    detail=f"Empresa {empresa['id']} não encontrada", code=404)
            obj_usuario.empresas.add(obj_empresa)

        print(obj_usuario.empresas)
        serializer = UsuarioSerializer(obj_usuario)

        return Response(serializer.data)
