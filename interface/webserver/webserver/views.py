import json
import os
from datetime import datetime, timedelta

import redis
import requests
from django.http import JsonResponse
from django.shortcuts import render
from webserver.connect_db_twitter import (conecta_com_mysql,
                                          obtem_lista_twitches)
from webserver.settings import BD_INFO


def get_ip(servico:str) -> str:
    
    # kubectl get services/consumidor-twitches-svc -o go-template='{{index .spec.ClusterIP}}'
    # Conecta no Banco
    r = redis.Redis(host='10.103.199.135')
    ip = r.get(servico).decode('utf8')
    
    # Cancela Conexao com DB
    del r
    
    # obtem IP do servico desejado
    return str(ip)

def realiza_request(host: str, pagina:str = "", parametros: dict = {}):
    
    prefixo_url = 'http://'
    
    # Realiza Request
    response = requests.get(prefixo_url + host + pagina, params=parametros)
    
    return response
    

def home(request):
    context = {
        'usuario': "Guilherme Pupio"
    }
    return render(request, 'webserver/home.html', context)

def requsicao_servico_teste(servico):
    parametros = { 'servico': servico }
    ip = get_ip("SIMULADOR_REQUESTS")
    return realiza_request(host=ip)

def servico_saudavel(request):
    """
        Realiza request em servico saudavel
    """
    context = {}
    try:
        response = requsicao_servico_teste(servico="teste")
        context['tempo_request_saudavel'] = json.loads(response.content)['Tempo_medio_por_request']
    except Exception:
        context['tempo_request_saudavel'] = "---"
    
    context['ultima_requisicao_saudavel']= datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    return JsonResponse(context)

def servico_teste(request):
    """
        Realiza request em servico de teste
    """
    
    context = {}
    try:
        response = requsicao_servico_teste(servico="teste")
        context['tempo_request_chaos'] = json.loads(response.content)['Tempo_medio_por_request']
    except Exception:
        context['tempo_request_chaos'] = "---"
    
    context['ultima_requisicao_chaos']= datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    return JsonResponse(context)


def render_status_servico(request):
    
    context= {
        'tempo_request_saudavel': "---ms",
        'tempo_request_chaos': "---ms",
        'ultima_requisicao_saudavel': datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'ultima_requisicao_chaos': datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    }
    
    return render(request,'webserver/servico1.html', context)


# COmando para obter nome dos pods 
# kubectl get pods -o wide | grep -E -o "(consumidor-twitches-deployment-)[a-z0-9]{10}-[a-z0-9]{5}"
