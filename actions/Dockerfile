FROM rasa/rasa_core_sdk:latest
ADD . /app/actions
ENTRYPOINT []
CMD python -m rasa_core_sdk.endpoint --actions actions.actions -p $PORT
