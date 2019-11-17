#!/bin/bash

# Obtem primeiro parametro
export nome="$1"

if [ "$nome" = 'latencia' ]; then
    export TIPO_TESTE="$nome"    
    echo "latencia"
fi

if [ "$nome" = 'perda_pacote' ]; then
    export TIPO_TESTE=$nome  
    echo "perda_pacote"
fi

# Obtem output dos requests
export output=$(curl http://104.155.179.191/request_teste/)

#export output='{"tempo_medio_resposta_chaos": "5.4e+01ms", "numero_requisicoes_realizadas_chaos": 1000, "numero_requisicoes_bem_sucedidas_chaos": "100.0%", "ultima_requisicao_chaos": "16:02:54 17/11/2019"}'

# Armazena tempo medio da resposta 
echo $output | jq '."tempo_medio_resposta_chaos"' > status_servidor_$TIPO_TESTE.log

# Registra saude das requiscoes
echo $output | jq '."numero_requisicoes_bem_sucedidas_chaos"' > status_servidor_saude_$TIPO_TESTE.log