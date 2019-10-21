#!/bin/bash

function main (){
    local nodeIp=`kubectl get nodes --selector=kubernetes.io/role!=master -o jsonpath={.items[*].status.addresses[?\(@.type==\"InternalIP\"\)].address}`
    local nodePort=`kubectl get svc my-consumer-service -o jsonpath={.spec.ports[0].nodePort}`

    export CONSUMER_ADDR=http://${nodeIp}:${nodePort}/
    echo "${CONSUMER_ADDR}"
}

main || exit 1
