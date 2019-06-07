

lta-tweetgen-win(){
winpty docker run -dit --rm --name data_server -v $spth:/home/ds/data --network lta-net simple-server //bin/bash
}

lta-tweetgen(){
  localpath=/home/devops/src/live-topic-analysis
  docker run -dit --rm --name tweet_gen \
         --env-file ./twitter.config \
         -v $localpath:/home/ds/data \
         --network lta-net thinkfulstudent/simple_server \
         python3.6 tweet_generator.py
}
