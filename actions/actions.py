from rasa_core_sdk import Action

class ActionHealth(Action):

    def name(self):
        return "action_health"

    def run(self, dispatcher, tracker, domain):
        service = next(tracker.get_latest_entity_values('service'), None)
        if service is not None:
            dispatcher.utter_message("You asked about {}".format(service))
        else:
            dispatcher.utter_message("I don't know what service you want!")
        
        return []