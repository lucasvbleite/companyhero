from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
import json
from .models import *

# Create your tests here.


class POSTTestCase(APITestCase):
    
    def setUp(self):
        self.empresa1 = Empresa.objects.create(nome="Company Hero1")
        self.empresa2 = Empresa.objects.create(nome="Company Hero2")
        self.empresa3 = Empresa.objects.create(nome="Company Hero3")
    
    def test_create_empresa1(self):
        data = {"nome": "Empresa1 Teste1"}
        response = self.client.post("/empresa/add/", json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_usuario_sem_empresa(self):

        data = {
            "username": "Teste"
        }

        response = self.client.post("/usuario/add/", json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_usuario_com_empresa(self):
        data = {
            "username": "Teste",
            "empresas": [
                {
                    "id": 1
                }
            ]
        }

        response = self.client.post("/usuario/add/", json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_usuario_com_empresas(self):

        data = {
            "username": "Teste",
            "empresas": [
                {
                    "id": 1
                },
                {
                    "id": 2
                },
                {
                    "id": 3
                }
            ]
        }

        response = self.client.post("/usuario/add/", json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_usuario_com_empresa_que_nao_existe(self):
    
        data = {
            "username": "Teste",
            "empresas": [
                {
                    "id": 1
                },
                {
                    "id": 2
                },
                {
                    "id": 3
                },
                {
                    "id": 4
                }
            ]
        }

        response = self.client.post("/usuario/add/", json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)