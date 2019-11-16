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
    return realiza_request(host=ip, parametros=parametros)

def gera_contexto(sufixo: str):
    context = {}
    try:
        response = requsicao_servico_teste(servico="teste")
        dict_response = json.loads(response.content)
        context['tempo_medio_resposta_' + sufixo] = "{0:.2}ms".format(dict_response['Tempo_medio_por_request']*1000)
        context['numero_requisicoes_realizadas_' + sufixo]= dict_response['Numero_Requisicoes']
        
        if "200" in dict_response['Ocorrencia_status_code'].keys():
            context['numero_requisicoes_bem_sucedidas_' + sufixo]= dict_response['Ocorrencia_status_code']["200"]
        else:
            context['numero_requisicoes_bem_sucedidas_' + sufixo]=0
            
    except Exception:
        context['tempo_medio_resposta_' + sufixo] = "---"
        context['numero_requisicoes_realizadas_' + sufixo]= 0
        context['numero_requisicoes_bem_sucedidas_' + sufixo]= 0
        
    
    context['ultima_requisicao_' + sufixo]= datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    
    return context
    

def servico_saudavel(request):
    """
        Realiza request em servico saudavel
    """
    context = gera_contexto("saudavel")
    return JsonResponse(context)

def servico_teste(request):
    """
        Realiza request em servico de teste
    """
    
    context = context = gera_contexto("chaos")
    return JsonResponse(context)


def render_status_servico(request):
    
    context= {
        'tempo_medio_resposta_saudavel': "---ms",
        'tempo_medio_resposta_chaos': "---ms",
        'ultima_requisicao_saudavel': datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'ultima_requisicao_chaos': datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    }
    
    return render(request,'webserver/servico1.html', context)


# COmando para obter nome dos pods 
# kubectl get pods -o wide | grep -E -o "(consumidor-twitches-deployment-)[a-z0-9]{10}-[a-z0-9]{5}"
