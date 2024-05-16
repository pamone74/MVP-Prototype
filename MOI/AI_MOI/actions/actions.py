# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionHandler(Action):
    def name(self) -> Text:
        return "action_handler"
    
    def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, 
Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'check_fines':
            return self.check_fines(dispatcher, tracker, domain)
        elif intent == 'renew_driving_license' or intent == "issuance_driving_license":
            return self.driving_license(dispatcher, tracker, domain)
        elif intent == 'criminal_record_certificate':
            return self.check_criminal_record_certificate(dispatcher, tracker, domain)
        elif intent == "renew_vehicle_registration":
            return self.renew_vehicle_registration(dispatcher, tracker, domain)
        return[]


    def check_fines(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Check_fines")
        return []
    
    def driving_license(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="driving_license")
        return []
    
    def check_criminal_record_certificate(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Check_criminal_record_certificate")
        return []
    
    def renew_vehicle_registration(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="renew_vehicle_registration")
        return []
    

class ValidateCheckFineForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_criminal_record_certificate_form"
    def validate_mobile_number(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if isinstance(slot_value, int) and len(str(slot_value)) == 10:
            return {"mobile_number": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid 10 digit mobile number")
            return {"mobile_number": None}
    def validate_email(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if "@" in slot_value:
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid email address")
            return {"email": None}
        
    def validate_emirates(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        emirates = ["Abu Dhabi", "Dubai", "Sharjah", "Ajman", "Umm Al Quwain", "Fujairah", "Ras Al Khaimah"]
        if slot_value in emirates:
            return {"emirates": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid emirates")
            return {"emirates": None}

    def validate_requesting_entity(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        if slot_value:
            return {"requesting_entity": slot_value}
        else:
            dispatcher.utter_message(text=f"Please enter a valid requesting entity")
            return {"requesting_entity": None}