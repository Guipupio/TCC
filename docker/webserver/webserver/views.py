import os

from django.http import JsonResponse
from django.shortcuts import render

from datetime import datetime

def home(request):
    context = {
        'usuario': "Guilherme Pupio"
    }
    return render(request, 'webserver/index.html', context)

def get_hostname(request):
    return JsonResponse({'Hostname': os.environ['HOSTNAME'] } )


def home_json(request):
    return JsonResponse({'Hora de Acesso: ': datetime.now()})