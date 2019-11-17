import os
from time import sleep, time

import numpy as np
import redis
import requests
from django.http import JsonResponse
from collections import Counter

dict_mapeamento_servico_ip = {
    'producao': "CONSUMIDOR_BD_IP",
    'teste': "CONSUMIDOR_BD_IP_TESTE"
}

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
def realiza_request(host: str, pagina:str = "/info_twitches/"):
    
    prefixo_url = 'http://'
    
    # Realiza Request
    response = requests.get(prefixo_url + host + pagina)
    
    return response.status_code
    
    


def get_ip(servico:str) -> str:
    
    # kubectl get services/consumidor-twitches-svc -o go-template='{{index .spec.ClusterIP}}'
    # Conecta no Banco
    r = redis.Redis(host='10.103.199.135')
    ip = r.get(servico).decode('utf8')
    
    # Cancela Conexao com DB
    del r
    
    # obtem IP do servico desejado
    return str(ip)
        
def simula_request(request):
    
    _request = request.GET if request.method == "GET" else request.POST
    warning = {}
    try:
        servico = str(_request.get("servico", "producao"))
        n_iteracoes = int(_request.get("num_iteracoes", 10))        
    except Exception as error:
        warning['ERRO-NUM_INTERACOES'] = str(error)
        n_iteracoes = 10
    # Obtem IP do servico 1
    ip_servico = get_ip(servico=dict_mapeamento_servico_ip[servico])
    
    # Define pagina acessada
    pagina = _request.get("pagina", '/info_twitches/')
    
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
        'Ocorrencia_status_code': dict_status,
        'Numero_Requisicoes': n_iteracoes,
        'warnings': warning,
        'servico_requisitado': servico
    }
    return JsonResponse(output)
