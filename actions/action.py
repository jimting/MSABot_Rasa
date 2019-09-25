class ActionWeather(Action):

    def name(self):
        return "action_weather"

    def run(self, dispatcher, tracker, domain):
        where = next(tracker.get_latest_entity_values('weather'), None)
        if where is not None:
            dispatcher.utter_message("You asked about {}".format(where))
        else:
            dispatcher.utter_message("I couldn't tell where!")
        
        return []