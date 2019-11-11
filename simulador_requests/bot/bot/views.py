import os
from time import sleep, time

import numpy as np
import redis
import requests
from django.http import JsonResponse
from collections import Counter


# Decorador para obter tempo de resposta das funcoes
def get_tempo_exec(func):
    def calcula_tempo(*args, **kwargs):
        t_init = time()
        resultado = func(*args, **kwargs)
        t_fim = time()

        tempo_execucao = t_fim - t_init
        # obtem a url da pagina
        return (resultado, tempo_execucao)
    return calcula_tempo

@get_tempo_exec
def realiza_request(host: str, pagina:str):
    
    prefixo_url = 'http://'
    pagina = "/info_twitches/"
    
    # Realiza Request
    response = requests.get(prefixo_url + host + pagina)
    
    return response.status_code
    
    


def get_ip(servico:str, type_service: str = "clusterIP") -> str:
    
    # kubectl get services/consumidor-twitches-svc -o go-template='{{index .spec.ClusterIP}}'
    # Conecta no Banco
    r = redis.Redis(host='10.111.168.116')
    ip = r.get("CONSUMIDOR_BD_IP").decode('utf8')
    
    # Cancela Conexao com DB
    del r
    
    # obtem IP do servico desejado
    return str(ip)
        
def simula_request(request):
    
    _request = request.GET if request.method == "GET" else request.POST
    
    n_iteracoes = _request.get("num_iteracoes", 1000)
    # Obtem IP do servico 1
    ip_servico = get_ip(servico="consumidor-twitches-svc")
    
    # Define pagina acessada
    pagina = _request.get("pagina", '')
    
    # Realiza Request
    lista_tempos = list(map(lambda x: realiza_request(host=ip_servico, pagina=pagina), list(range(n_iteracoes))))
    np_lista_info = np.array(lista_tempos)
    
    # Obtem a lista de status
    response_status = np_lista_info[:,0]
    total_requests = len(response_status)
    
    # Agrupa status com sua ocorrencia
    ocorrencia_status = dict(Counter(response_status))
 
    dict_status = {str(int(status)): str(count*100/total_requests) + "%" for status, count in ocorrencia_status.items()}
        
    output = {
        'Tempo_medio_por_request': np_lista_info[:,1].mean(),
        'Ocorrencia_status_code': dict_status
    }
    return JsonResponse(output)
