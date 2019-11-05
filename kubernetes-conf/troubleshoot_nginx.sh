kubectl create clusterrolebinding nginx-ingress-admin -n nginx-ingress  --clusterrole=cluster-admin  --serviceaccount=nginx-ingress:nginx-ingress
