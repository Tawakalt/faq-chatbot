# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List


class SalesForm(FormAction):
    """Collects sales info and adds it to the spreadsheet"""

    def name(self):
        return "sales_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "job_function",
            "use_case",
            "budget",
            "person_name",
            "company",
            "business_email",
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we'll contact you soon")
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
    """
    A dictionary to map required slots to
    - an extracted entity
    - intent: value pairs
    - a whole message
    or a list of them, where a first match will be picked
    """
    return {"use_case": self.from_text(intent="inform")}
