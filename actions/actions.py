from rasa_core_sdk import Action
import json

class ActionHealth(Action):

    def name(self):
        return "action_service_health"

    def run(self, dispatcher, tracker, domain):
        service = next(tracker.get_latest_entity_values('service'), None)
		searching_service = ""
        if service is not None:
            searching_service = service
        else:
            searching_service = "none"
		data = {
			"intent" : "action_service_health",
			"service" : searching_service
		}
        dispatcher.utter_message(data)
        return []
		
class ActionInfo(Action):

    def name(self):
        return "action_service_info"

    def run(self, dispatcher, tracker, domain):
        service = next(tracker.get_latest_entity_values('service'), None)
		searching_service = ""
        if service is not None:
            searching_service = service
        else:
            searching_service = "none"
		data = {
			"intent" : "action_service_info",
			"service" : searching_service
		}
        dispatcher.utter_message(data)
        return []

class ActionUsingInfo(Action):

    def name(self):
        return "action_service_using_info"

    def run(self, dispatcher, tracker, domain):
        service = next(tracker.get_latest_entity_values('service'), None)
		searching_service = ""
        if service is not None:
            searching_service = service
        else:
            searching_service = "none"
		data = {
			"intent" : "action_service_using_info",
			"service" : searching_service
		}
        dispatcher.utter_message(data)
        return []

class ActionApiList(Action):

    def name(self):
        return "action_service_api_list"

    def run(self, dispatcher, tracker, domain):
        service = next(tracker.get_latest_entity_values('service'), None)
		searching_service = ""
        if service is not None:
            searching_service = service
        else:
            searching_service = "none"
		data = {
			"intent" : "action_service_api_list",
			"service" : searching_service
		}
        dispatcher.utter_message(data)
        return []