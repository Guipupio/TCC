import os

from django.http import JsonResponse
from django.shortcuts import render

from datetime import datetime, timedelta
from webserver.settings import BD_INFO

from webserver.connect_db_twitter import conecta_com_mysql, obtem_lista_twitches

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

def home(request):
    context = {
        'usuario': "Guilherme Pupio"
    }
    return render(request, 'webserver/base_generic.html', context)

def get_hostname(request, auxiliar_request=False):
    RAM_INFO = os.popen('free -t -m -h | grep Mem:').readlines()[0]
    RAM_INFO = [info for info in RAM_INFO.split(' ') if info != '']
    
    # Tenta obter hostname
    try:
        hostname = os.environ['HOSTNAME']
    except KeyError:
        hostname = list(os.environ.keys())
    infos = {
        'Hostname': hostname,
        'CPU Use': '{}%'.format(str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))),
        'RAM Use':  'Usado: {}; Total: {}'.format(RAM_INFO[2], RAM_INFO[1])
    }
    
    if auxiliar_request:
        return infos
    else:
        return JsonResponse(infos)


def home_json(request):
    return JsonResponse({'Hora de Acesso: ': datetime.now()})

def get_twitches(request):
    """
        Realiza consulta no banco e retorna alguma coisa baseado nos Twitches
        TODO - Definar banco de Dados        
        TODO - Fazer alguma coisa com os dados
    """
    
    # Define contexto inicialmente vazio
    context = {}
    
    # Obtem request, independetemente do metodo de requisicao (GET, POST)
    _request = request.POST if request.method == 'POST' else request.GET
    
    # Estabelece Conexao com banco de Dados
    connection = conecta_com_mysql(host=BD_INFO['HOST'], database=BD_INFO['NAME'], user=BD_INFO['USER'], password=BD_INFO['PASSWORD'])
    # Obtem lista de twitches armazendas no BD
    lista_twitches = obtem_lista_twitches(connection)
    
    # Caso o usuario deseje um status do POD
    if _request.get('infos_pod', False):
        context = dict(context, **get_hostname(request,auxiliar_request=True))
    
    context['twitches'] = lista_twitches
    
    return JsonResponse(context)

def servico_um(request):
    context= {
        'tempo_request': "20ms",
        'ultima_requisicao': datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    }
    return render(request,'webserver/servico1.html', context)