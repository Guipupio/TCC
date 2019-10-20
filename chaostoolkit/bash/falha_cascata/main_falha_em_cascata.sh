# Obtem a url do servico
HOSTS_MICRO_SERVICO=$(./get-host-address)
export URL=$($HOSTS_MICRO_SERVICO | tr " " "\n" | grep http)
export PORT= $($HOSTS_MICRO_SERVICO | tr ":" "\n" | grep "[0-9][0-9][0-9][0-9][0-9]")
echo "URL: $URL:$PORT"
#curl --write-out %{http_code} --silent --output /dev/null http://10.128.0.10:31212/