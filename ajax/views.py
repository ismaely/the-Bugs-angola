from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.http import JsonResponse
import random, json
# Create your views here.

def remove_privilege_categoria(request):
    try:
        dados = dict()
        if request.method == 'POST':
            valor = []
            valor = request.body.decode('utf-8')
            valor = json.loads(valor)
            grupo = valor['groupo']
            listaPerm = valor['lista_perm']

            if(len(valor['lista_perm']) > 1):
                group = Group.objects.get(id=grupo)
                for aux in listaPerm:
                    perm = Permission.objects.get(id=aux)
                    group.permissions.remove(perm)
            else:
                
                aux = listaPerm.split('-') # o valor é exemplo #-23
                group = Group.objects.get(id=grupo)
                perm = Permission.objects.get(id=aux[1])
                group.permissions.remove(perm)

            dados = {
                'resp':  True,
            }
        return JsonResponse(dados)
    except ValueError:
        print("Não foi possivel eliminar permisão")