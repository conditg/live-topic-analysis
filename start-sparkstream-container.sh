lta-sparkstream-start-win(){
winpty docker run -dit --rm --name spark_stream -v $spth:/home/jovyan --network lta-net jupyter/pyspark-notebook //bin/bash
}

lta-sparkstream-start(){
  localpath=/home/devops/src/live-topic-analysis
  docker run -it --rm --name spark_stream \
         -u 0 \
         -v $localpath:/home/jovyan \
         --network lta-net jupyter/pyspark-notebook \
         python spark_streaming.py 
}
         #/bin/bash
         #-u $(stat -c "%u:%g" ./cps) \
