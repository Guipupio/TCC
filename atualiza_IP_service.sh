# Cria servicos
kubectl create -f service.yaml

# Obtem IP do consumidor
export CONSUMIDOR_BD_IP=$(kubectl get svc consumidor-twitches-svc | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+')

# Grava no REDIS o valor da variavel
redis-cli -h 10.111.168.116 set CONSUMIDOR_BD_IP $CONSUMIDOR_BD_IP

