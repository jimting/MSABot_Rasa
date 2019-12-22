FROM rasa/rasa_nlu:latest-spacy

RUN pip install -U $(pip freeze | cut -d '=' -f 1)