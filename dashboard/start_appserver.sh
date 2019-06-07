lta-app-start-win(){
winpty docker run -dit --rm --name app_server -v $spth\\dashboard:/home/ds/data -p 9991:9991 --network lta-net simple-flask //bin/bash
}

lta-app-start(){
  lta_server_path=/home/devops/src/live-topic-analysis/dashboard
  docker run -d --rm --name app_server \
  -v $lta_server_path:/home/ds/data -p 9991:9991 \
  --network lta-net simple-flask
}

lta-app-build() {
  docker build -t simple-flask .
}

