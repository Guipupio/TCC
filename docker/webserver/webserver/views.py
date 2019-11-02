from django.shortcuts import render

def home(request):
    context = {
        'usuario': "Guilherme Pupio"
    }
    return render(request, 'webserver/index.html', context)