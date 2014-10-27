curl -sSL https://get.docker.io/ | sh

docker ps -aq | xargs -r docker rm
docker images -q | xargs -r docker rmi

echo "DOCKER_OPTS=\"-H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock\"" >> /etc/default/docker

