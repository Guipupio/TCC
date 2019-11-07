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
def realiza_request(url: str):
    sleep(0.5)

def simula_request(request):
    
    _request = request.GET if request.method == "GET" else request.POST
    
    n_iteracoes = _request.get("num_iteracoes", 5)
    # Obtem IP do servico 1
    
    # Realiza Request
    lista_tempos = [realiza_request('blabla')[1] for i in range(n_iteracoes)]
    
    return JsonResponse({'tempo_medio': np.array(lista_tempos).mean()})