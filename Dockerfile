FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install rasa-core 
RUN pip3 install rasa-nlu[tensorflow] 
RUN pip3 install spacy 
RUN pip3 install sklearn-crfsuite 
RUN pip3 install rasa-core-sdk
RUN python3 -m spacy download en

ADD ./models /app/models/
ADD ./config /app/config/
ADD ./actions /app/actions/
ADD ./scripts /app/scripts/

ENTRYPOINT []
CMD python3 -m rasa_core_sdk.endpoint --actions app.actions.actions 
CMD python3 -m rasa_core.run --enable_api --core /app/models/rasa_core -u /app/models/rasa_nlu/current/nlu --endpoints /app/config/endpoints.yml --credentials /app/config/credentials.yml -p $PORT
# python3 -m rasa_nlu.train -c config/nlu_config.yml -d data/nlu.md --fixed_model_name nlu -o models/rasa_nlu --project current
