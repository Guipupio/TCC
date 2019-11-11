import os

from django.http import JsonResponse
from django.shortcuts import render

from datetime import datetime, timedelta
from webserver.settings import BD_INFO

from webserver.connect_db_twitter import conecta_com_mysql, obtem_lista_twitches


def home(request):
    context = {
        'usuario': "Guilherme Pupio"
    }
    return render(request, 'webserver/home.html', context)

def servico_saudavel(request):    
    context= {
        'tempo_request_saudavel': "20ms",
        'tempo_request_chaos': "40ms",
        'ultima_requisicao_saudavel': datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'ultima_requisicao_chaos': (datetime.now() + timedelta(seconds=1234)).strftime('%H:%M:%S %d/%m/%Y')
    }
    if request.method == "GET":
        return render(request,'webserver/servico1.html', context)
    elif request.method =="POST":
        return JsonResponse(context)
    else:
        return JsonResponse({})