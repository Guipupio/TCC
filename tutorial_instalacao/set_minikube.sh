# Tutorial de Instalacao do Kubernetes

# Baixe o kubernete:
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

# Tornando o kubctl executável
chmod +x ./kubectl

# Movendo o kubectl ao PATH do sistema
sudo mv ./kubectl /usr/local/bin/kubectl

# Teste para verificar se a instalacao do kubectl ocorreu corretamente
kubectl version

# Baixe o minikube e de as permissoes de executavel
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube

# Adicionando minikube ao path do sistema
sudo mkdir -p /usr/local/bin/ && sudo install minikube /usr/local/bin/

# Teste para verificar se a instalacao do minikube do ocorreu corretamente
minikube version