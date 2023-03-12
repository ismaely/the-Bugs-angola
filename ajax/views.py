from django.shortcuts import render
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
            groupo = valor['groupo']
            perm = valor['lista_perm']
            print(groupo)
            print(perm)
            dados = {
                '200':  True,
            }
        return JsonResponse(dados)
    except ValueError:
        print("Não foi possivel eliminaar")