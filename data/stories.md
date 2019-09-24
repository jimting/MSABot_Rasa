## happy_path
* greet
  - utter_greet
* mood_happy
  - utter_happy
* goodbye
  - utter_goodbye
  - action_restart

## sad_path
* greet
  - utter_greet
* mood_unhappy
  - actions.ActionJoke
* goodbye
  - utter_goodbye
  - action_restart
