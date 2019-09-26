from rasa_core_sdk import Action

class ActionGetWeather(Action):

    def name(self):
        return 'action_get_weather'

    def run(self, dispatcher, tracker, domain):
        where = ('Auckland', tracker.get_slot('GPE'))[bool(tracker.get_slot('GPE'))]
        if where is not None:
            dispatcher.utter_message("You asked about {}".format(where))
        else:
            dispatcher.utter_message("I don't know where!")
        return