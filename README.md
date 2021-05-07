# Teste Company Hero

Esse repositório contém o código utilizado no teste da Company Hero.

O teste consistia em criar duas entidades, Empresa e Usuario, com seus respectivos GETs e POSTs.\
Os usuários poderiam se cadastrar em mais de uma empresa.\
As Empresas deveriam trazer seus usuários.\
Os Usuários deveriam trazer suas empresas.

Solução\
Fiz duas models, Empresa e Usuario, onde a Usuario é relacionada à Empresa por uma relação ManyToMany.\
Fiz o GET e o POST pra essas duas models.

A URL é https://teste-company-hero-2021.herokuapp.com

## Empresa
GET - https://teste-company-hero-2021.herokuapp.com/empresa

Lista todas as empresas e seus usuários

POST - https://teste-company-hero-2021.herokuapp.com/empresa/add/

exemplo:
```
{
    "nome" : "Teste"
}
```

## Usuário
GET - https://teste-company-hero-2021.herokuapp.com/usuario

Lista todos os usuários e suas empresas

POST - https://teste-company-hero-2021.herokuapp.com/usuario/add/

exemplo:
```
{
    "username" : "Teste",
    "empresas" : [
        {
            "id" : 1
        }
    ]
}
```
