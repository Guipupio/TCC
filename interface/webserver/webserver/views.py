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
    return render(request, 'webserver/base_generic.html', context)

def servico_um(request):
    context= {
        'tempo_request': "20ms",
        'ultima_requisicao': datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    }
    return render(request,'webserver/servico1.html', context)