kubectl get deployments.app |grep my-provider-app|grep -o -E '[0-9]/[0-9]' > num_pods.log