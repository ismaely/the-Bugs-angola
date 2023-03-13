from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.http import JsonResponse
import random, json
# Create your views here.


# Função que vai remover privilegios de um determinado utilizador 
def remove_privilege_user(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            userId = valor['groupo']
            listaPerm = valor['lista_perm']

            if("#" in str(listaPerm)):
                aux = str(listaPerm) # o valor  é exemplo #-22
                ids = aux.split('-') # ['#', 'valor'] separando os valores
                respUser = User.objects.get(id=userId)
                perm = Permission.objects.get(id=int(ids[1]))
                respUser.user_permissions.remove(perm)
                
            else:
                respUser = User.objects.get(id=userId)
                for aux in listaPerm:
                   perm = Permission.objects.get(id=aux)
                   respUser.user_permissions.remove(perm)

            dados = {'200': True }
            return JsonResponse(dados)
    except Exception as e:
        print("Não foi possivel eliminar permisão user")



# remover a permisão de um terminado grupo
def remove_privilege_categoria(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            grupo = valor['groupo']
            listaPerm = valor['lista_perm']

            if("#" in str(listaPerm)):
                aux = str(listaPerm) # o valor  é exemplo #-22
                ids = aux.split('-')  # ['#', 'valor'] separando os valores
                group = Group.objects.get(id=grupo)
                perm = Permission.objects.get(id=int(ids[1]))
                group.permissions.remove(perm)
                
            else:
                group = Group.objects.get(id=grupo)
                for aux in listaPerm:
                   perm = Permission.objects.get(id=aux)
                   group.permissions.remove(perm)

            dados = {'200': True }
            return JsonResponse(dados)
    except Exception as e:
        print("Não foi possivel eliminar permisão")