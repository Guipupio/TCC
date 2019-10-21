#!/bin/bash

# Obtem a url do servico
HOSTS_MICRO_SERVICO=$(./get-host-address.sh)
# Obtem HOST http://IP
IP_ENCONTRADO=$(echo "$HOSTS_MICRO_SERVICO" | tr " " "\n" | grep http)
# Obtem Porta [0-9  ]
PORT_ENCONTRADA=$(echo "$HOSTS_MICRO_SERVICO" | tr ":" "\n" | grep "[0-9]\{5\}")
# Define a URL de Acesso
export URL="$IP_ENCONTRADO:$PORT_ENCONTRADA"

# Ativa virtualEnv e # Inicia teste do chaos toolkit
activate && chaos run /home/guicpupio/tcc/chaostoolkit/falha_cascata/json/teste_servicos_em_cascata.json

