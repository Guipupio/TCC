from os import environ

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    context = {
        'usuario': "Guilherme Pupio"
    }
    return render(request, 'webserver/index.html', context)

def get_hostname(request):
    return JsonResponse({'Hostname': environ['HOSTNAME'] } )
