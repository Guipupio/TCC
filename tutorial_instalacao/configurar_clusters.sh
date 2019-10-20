# Para setar o cluster master
# OBS: Desde Comando sera informado o comando para conectar as maquinas slaves neste cluster
kubeadm init --apiserver-advertise-address $(hostname -i)

# Criacao de de estrutura de diretorios
mkdir -p $HOME/.kube

# Copia das configuracaoes do kubernetes para comunicacao do kubectl
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

# Altera as permissoes das configuracoes copiadas
sudo chown $(id -u):$(id -g) $HOME/.kube/config



## ----------------- NAS MAQUINAS SLAVES -----------------
# Nota este comando pode ser diferente.. pois ele eh informado a paritir do primeiro comando deste arquivo
kubeadm join 10.128.0.10:6443 --token xws0a5.bpzv3ojm5pohq19k     --discovery-token-ca-cert-hash sha256:130a4d8dbde047efad28fe446214d5fd71e74862e73b942918f907c9815d646e

## ----------------- NA MASTER -----------------
## Realizar deploy do POD Network, responsavel por estabelecer uma comunicacao entre os PODS
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"

# Realiza deploy de PODs com imagens do nginx, de namespace nginx.
# eh Possivel adicionar o parametro --replicas x, onde x eh o numero de replicas
kubectl run nginx --image nginx --port 80

# Cria servico para o deployment nginx (podemos fazer isso para PODs)
kubectl expose deployment nginx