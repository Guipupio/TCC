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
    RAM_INFO = os.popen('free -t -m -h | grep Mem:').readlines()[0]
    RAM_INFO = [info for info in RAM_INFO.split(' ') if info != '']
    infos = {
        'Hostname': os.environ['HOSTNAME'],
        'CPU Use': '{}%'.format(str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))),
        'RAM Use':  'Usado: {}; Total: {}'.format(RAM_INFO[2], RAM_INFO[1])
    }
    return JsonResponse(infos)


def home_json(request):
    return JsonResponse({'Hora de Acesso: ': datetime.now()})