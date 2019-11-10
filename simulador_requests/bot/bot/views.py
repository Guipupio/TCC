import os
from time import time, sleep
from django.http import JsonResponse
 
import numpy as np

import requests

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
    sleep(0.001)
    
    prefixo_url = 'http://'
    pagina = "/info_twitches/"
    
    # Realiza Request
    response = requests.get(prefixo_url + host + pagina)
    
    return response.status_code
    
    


def get_ip(servico:str, type_service: str = "clusterIP") -> str:
    
    # kubectl get services/consumidor-twitches-svc -o go-template='{{index .spec.ClusterIP}}'
    commando = "kubectl get services/{servico} -o go-template='{abre_chaves}(index .spec.{type_service}){fecha_chaves}'".format(servico=servico, type_service=type_service, abre_chaves= '{{',
fecha_chaves= '}}')
    
    # obtem IP do servico desejado
    return os.popen(commando).read()
        
def simula_request(request):
    
    _request = request.GET if request.method == "GET" else request.POST
    
    n_iteracoes = _request.get("num_iteracoes", 1000)
    # Obtem IP do servico 1
    ip_servico = get_ip(servico="consumidor-twitches-svc")
    
    # Define pagina acessada
    pagina = _request.get("pagina", '')
    
    # Realiza Request
    lista_tempos = list(map(lambda x: realiza_request(host=ip_servico, pagina=pagina), list(range(n_iteracoes))))
    
    return JsonResponse({'tempo_medio': np.array(lista_tempos)[:,0].mean()})