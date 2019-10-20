## ---------- SET MAQUINAS VIRTUAIS MAQUINAS VIRTUAIS ------------
# Atualizamos os repositorios das maquinas do Google Cloud
apt-get update

#Desligamos o swap das maquinas
swapoff -a

# Intalando Docker nas VMs do Google Cloud
curl -fsSL https://docs.docker.com | bash

# Chave do repositorio com comandos do kubernetes
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -

# ADicionamos o repositorio
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list

# Baixamos a lista de pacotes disponiveis no novo repositorio instalado
apt-get update

# Instalamos os comandos necessarios do kubernetes
# kubeadm - responsavel por montar o cluster
# kubectl - resposavel por operar/iteragir com o cluster
# kubelet - como se fosse um agente operando em todos os nos, conversando com o nó master
apt-get install -y kubelet kubeadm kubectl
