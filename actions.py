# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

#from .calendarTest import create_event
#from ipynb.fs.full.calendarTest import factorial
from .calendarr import create_event
#import calendarr

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!from action")

        return []

class ActionHelloWorld(FormAction):

    def name(self) -> Text:
        return "meeting_request_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["partcipant_email","meeting_subject","meeting_time","meeting_date"]
    
    create_event("12 january 10 PM", "MeetingTest2",0.5,"testing","ISB")
    
    def submit(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any],
              ) -> List[Dict]:
        dispatcher.utter_message("Form Filled!")
        return []
