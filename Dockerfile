FROM rasa/rasa-sdk:latest

RUN pip3 install rasa-core 
RUN pip3 install rasa-nlu[tensorflow] 
RUN pip3 install spacy 
RUN pip3 install sklearn-crfsuite 
RUN pip3 install rasa-core-sdk
RUN python3 -m spacy download en

ADD ./models /app/models/
ADD ./config /app/config/

ENTRYPOINT []

CMD python3 -m rasa_core_sdk.endpoint --actions app.actions.actions 
CMD python3 -m rasa_core.run --enable_api --core /app/models/rasa_core -u /app/models/rasa_nlu/current/nlu --endpoints /app/config/endpoints.yml --credentials /app/config/credentials.yml -p $PORT